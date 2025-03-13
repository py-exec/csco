from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from .forms import CartonForm, CartonFilterForm
from .width_optimizer import WidthOptimizer
from .calculate_b01_b_carton import CartonCalculator
from .models import Carton, Customer
import json


class CartonFormView(View):
    template_name = "carton_form.html"

    def get(self, request):
        """ نمایش فرم سفارش با لیست مشتریان موجود """
        form = CartonForm()
        form.fields['customer'].queryset = Customer.objects.all()  # نمایش لیست مشتریان
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        print("📌 داده‌های دریافتی:", request.POST)

        # **۱. دریافت شماره مشتری از فرم و پیدا کردن مشتری در دیتابیس**
        customer_phone = request.POST.get("customer", "").strip()
        customer = Customer.objects.filter(phone=customer_phone).first()

        if not customer:
            messages.error(request, "❌ مشتری انتخاب‌شده معتبر نیست! لطفاً از لیست مشتریان انتخاب کنید.")
            return render(request, self.template_name, {"form": CartonForm()})

        # **۲. ایجاد نسخه‌ی کپی از `request.POST` و تغییر مقدار `customer`**
        mutable_post = request.POST.copy()
        mutable_post["customer"] = customer.id  # جایگذاری مقدار `id` مشتری

        # **۳. مقداردهی فرم با داده‌های اصلاح‌شده**
        form = CartonForm(mutable_post)

        if not form.is_valid():
            print("❌ فرم نامعتبر است! خطاها:", form.errors)
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"❌ {form.fields[field].label}: {error}")

            messages.error(request, "⚠️ خطا در فرم! لطفاً فیلدهای موردنیاز را پر کنید.")
            return render(request, self.template_name, {"form": form, "error_messages": error_messages})

        try:
            # **۴. دریافت داده‌های تمیز شده و مقداردهی پیش‌فرض**
            cleaned_data = form.cleaned_data
            layer_count = cleaned_data.get("layer_count", None)

            if layer_count is None:
                messages.error(request, "❌ مقدار تعداد لایه نمی‌تواند خالی باشد!")
                return render(request, self.template_name, {"form": form})

            # **۵. ذخیره سفارش در دیتابیس**
            new_order = Carton.objects.create(
                model=cleaned_data.get("model", ""),
                order_quantity=cleaned_data.get("order_quantity", 0),
                length=cleaned_data.get("length", 0),
                width=cleaned_data.get("width", 0),
                height=cleaned_data.get("height", 0),
                time=cleaned_data.get("time", ""),
                top_color=cleaned_data.get("top_color", ""),
                material_combination=cleaned_data.get("material_combination", ""),
                printing=cleaned_data.get("printing", ""),
                color_count=cleaned_data.get("color_count", ""),
                joining=cleaned_data.get("joining", ""),
                sheet_roll=cleaned_data.get("sheet_roll", ""),
                coating=cleaned_data.get("coating", ""),
                packaging=cleaned_data.get("packaging", ""),
                customer=customer,
                layer_count=layer_count,  # مقداردهی `layer_count`
            )

            messages.success(request, f"✅ سفارش شماره {new_order.id} با موفقیت ثبت شد!")
            return redirect(self.get_success_url())

        except Exception as e:
            messages.error(request, f"❌ خطا در ثبت سفارش: {str(e)}")
            return render(request, self.template_name, {"form": form})

    def get_success_url(self):
        return "/calculator/CartonOrdernew/"

@require_POST  # فقط درخواست‌های POST را قبول کند
def add_customer_ajax(request):
    """ اضافه کردن مشتری جدید با نام و شماره موبایل (فقط با CSRF Token معتبر) """
    if not request.META.get("HTTP_X_CSRFTOKEN"):  # چک کردن توکن CSRF
        return JsonResponse({"success": False, "error": "CSRF Token یافت نشد!"}, status=403)

    try:
        data = json.loads(request.body)  # دریافت داده‌های JSON
        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()

        # چک کردن مقداردهی نام و شماره موبایل
        if not name or not phone:
            return JsonResponse({"success": False, "error": "نام و شماره موبایل الزامی است!"}, status=400)

        # بررسی اینکه شماره موبایل یونیک است
        customer, created = Customer.objects.get_or_create(phone=phone, defaults={"name": name})

        if not created:
            return JsonResponse({"success": False, "error": "شماره موبایل قبلاً ثبت شده است!"}, status=400)

        return JsonResponse({"success": True, "id": customer.id, "name": customer.name, "phone": customer.phone})

    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "فرمت داده‌ها نادرست است!"}, status=400)


@require_POST
def get_customers_ajax(request):
    """ دریافت لیست مشتریان (با شماره موبایل و نام) """
    if not request.META.get("HTTP_X_CSRFTOKEN"):  # چک کردن CSRF Token
        return JsonResponse({"success": False, "error": "CSRF Token یافت نشد!"}, status=403)

    customers = list(Customer.objects.values("id", "name", "phone"))
    return JsonResponse({"success": True, "customers": customers})


def get_csrf_token(request):
    """ دریافت CSRF Token برای استفاده در درخواست‌های AJAX """
    return JsonResponse({"csrfToken": get_token(request)})


class WidthOptimizerView(View):
    """ویو برای محاسبه بهترین عرض ورق با استفاده از کلاس WidthOptimizer"""

    def __init__(self, request):
        try:
            self.layer_count = int(request.GET.get("layer_count"))
            self.user_defined_width = float(request.GET.get("user_defined_width"))
            self.requested_group = request.GET.get("requested_group").strip()
        except (ValueError, AttributeError, TypeError):
            self.layer_count = None
            self.user_defined_width = None
            self.requested_group = None
            self.error = {"status": "error", "message": "ورودی‌های نامعتبر!"}
        else:
            self.error = None

    def get_response(self):
        """اجرای فرآیند محاسبه و ارائه خروجی به‌صورت دیکشنری"""
        if self.error:
            return self.error

        optimizer = WidthOptimizer(self.layer_count, self.user_defined_width, self.requested_group)
        return optimizer.get_results()


class CartonCalculatorView(View):
    """ویو برای محاسبه گسترده کارتن B01+1 با استفاده از کلاس CartonCalculator"""

    def __init__(self, request):
        try:
            self.layer_count = int(request.GET.get("layer_count"))
            self.flute_type = request.GET.get("flute_type")
            self.input_type = request.GET.get("input_type").strip()
            self.length = float(request.GET.get("length"))
            self.width = float(request.GET.get("width"))
            self.height = float(request.GET.get("height"))
        except (ValueError, AttributeError, TypeError):
            self.layer_count = None
            self.flute_type = None
            self.input_type = None
            self.length = None
            self.width = None
            self.height = None
            self.error = {"status": "error", "message": "ورودی‌های نامعتبر!"}
        else:
            self.error = None

    def get_response(self):
        """اجرای فرآیند محاسبه و ارائه خروجی به‌صورت دیکشنری"""
        if self.error:
            return self.error

        calculator = CartonCalculator(self.length, self.width, self.height, self.layer_count, self.flute_type, self.input_type)
        return calculator.get_results()


class CartonOrderListView(View):
    template_name = "carton_order_list.html"

    def get(self, request):
        # print("DEBUG: customer value received ->", request.GET.get("customer"))  # ✅ دیباگ مقدار دریافت شده
        form = CartonFilterForm(request.GET)
        orders = Carton.objects.all().order_by("-id")

        if form.is_valid():
            if form.cleaned_data["customer"]:
                orders = orders.filter(customer=form.cleaned_data["customer"])  # ✅ بررسی مقدار customer
            if form.cleaned_data["model"]:
                orders = orders.filter(model=form.cleaned_data["model"])
            if form.cleaned_data["top_color"]:
                orders = orders.filter(top_color=form.cleaned_data["top_color"])
            if form.cleaned_data["from_date"]:
                orders = orders.filter(created_at__gte=form.cleaned_data["from_date"])
            if form.cleaned_data["to_date"]:
                orders = orders.filter(created_at__lte=form.cleaned_data["to_date"])

        return render(request, self.template_name, {"form": form, "orders": orders})

