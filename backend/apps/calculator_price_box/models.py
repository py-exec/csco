from django.db import models
from django.utils.timezone import now

# افزودن ارتباط مشتری به قیمت‌گذاری سفارش
from apps.customer.models import Customer

# 📌 مدل انتخاب عرض ورق
class WidthSelection(models.Model):
    group_name = models.CharField(max_length=50, verbose_name="نام گروه")
    width_title = models.CharField(max_length=50, verbose_name="عنوان عرض")
    width_value = models.IntegerField(verbose_name="مقدار عرض (میلی‌متر)")
    available = models.BooleanField(default=True, verbose_name="موجود")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    def __str__(self):
        return f"{self.width_title} - {self.width_value}mm"


# 📌 مدل تبدیل ابعاد داخلی به خارجی و بالعکس B01+B
class DimensionConversionB01B(models.Model):
    flute = models.CharField(verbose_name="نوع فلوت")
    length_internal_external = models.FloatField(verbose_name="طول داخلی به خارجی")
    width_internal_external = models.FloatField(verbose_name="عرض داخلی به خارجی")
    height_internal_external = models.FloatField(verbose_name="ارتفاع داخلی به خارجی")
    length_external_internal = models.FloatField(verbose_name="طول خارجی به داخلی")
    width_external_internal = models.FloatField(verbose_name="عرض خارجی به داخلی")
    height_external_internal = models.FloatField(verbose_name="ارتفاع خارجی به داخلی")
    available = models.BooleanField(default=True, verbose_name="موجود")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    def __str__(self):
        return f"تبدیل {self.flute.flute_type}"



# 📌 مدل اصلی سفارش کارتن
class Carton(models.Model):
    """مدل سفارش کارتن با فیلدهای کامل و استاندارد"""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="مشتری")
    model = models.CharField(max_length=50, verbose_name="مدل کارتن")
    order_quantity = models.PositiveIntegerField(verbose_name="تعداد سفارش")
    dimension_type = models.CharField(max_length=50, verbose_name="نوع ابعاد")
    length = models.FloatField(verbose_name="طول (سانتی‌متر)")
    width = models.FloatField(verbose_name="عرض (سانتی‌متر)")
    height = models.FloatField(verbose_name="ارتفاع (سانتی‌متر)")
    time = models.CharField(max_length=50, verbose_name="زمان تحویل")
    top_color = models.CharField(max_length=50, verbose_name="رنگ رویه")
    layer_count = models.IntegerField(verbose_name="تعداد لایه")
    flute = models.CharField(max_length=50, verbose_name="نوع فلوت")
    material_combination = models.CharField(max_length=50, verbose_name="ترکیب متریال")
    printing = models.CharField(max_length=50, verbose_name="نوع چاپ")
    sheet_roll = models.CharField(max_length=50, blank=True, null=True, verbose_name="شیت/رول")
    coating = models.CharField(max_length=50, blank=True, null=True,verbose_name="روکش")
    color_count = models.PositiveIntegerField(blank=True, null=True, verbose_name="تعداد رنگ")
    joining = models.CharField(max_length=50, blank=True, null=True, verbose_name="روش اتصال")
    group_selection = models.CharField(max_length=50, verbose_name="انتخاب گروه")
    packaging = models.CharField(max_length=50, verbose_name="بسته‌بندی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت سفارش")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    def __str__(self):
        return f"{self.model} - {self.order_quantity} عدد - {self.customer.name}"