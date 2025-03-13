from django import forms
from .models import Carton, Customer
from django_select2.forms import Select2Widget

class CartonForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        label="انتخاب مشتری",
        widget=Select2Widget(attrs={'data-placeholder': "جستجو کنید...", 'class': 'form-control'})
    )

    new_customer_name = forms.CharField(
        max_length=255,
        label="نام مشتری جدید (در صورت اضافه کردن مشتری جدید)",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required = False,

    )

    # ✅ مقداردهی فیلدهای `ChoiceField` بدون تغییر `id`
    model = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("B01+B", "B01+B"), ("D27", "D27"), ("B15", "B15"),
            ("B11", "B11"), ("B17", "B17"), ("B01+D", "B01+D"),
            ("B00", "B00"), ("B03", "B03")
        ],
        label="مدل",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    time = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("1w", "یک هفته"), ("2w", "دو هفته"),
            ("4w", "چهار هفته"), ("shop", "فروشگاه")
        ],
        label="زمان تحویل",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    top_color = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("brown", "قهوه‌ای"), ("white", "سفید"), ("laminate", "لمینت")
        ],
        label="رنگ رویه",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    layer_count = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("3", "3 لایه"), ("5", "5 لایه")
        ],
        label="تعداد لایه",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    dimension_type = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("internal", "داخلی"), ("external", "خارجی")
        ],
        label="نوع ابعاد",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    flute = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("B", "B"), ("C", "C"), ("E", "E"), ("BC", "BC"), ("EB", "EB"), ("EC", "EC")
        ],
        label="فلوت",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    material_combination = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("Brown Eco", "Brown Eco"), ("Brown", "Brown"),
            ("Brown TOP", "Brown TOP"), ("Brown BEST", "Brown BEST"),
            ("Brown Heavy", "Brown Heavy"), ("Brown VIP", "Brown VIP"),
            ("White Eco", "White Eco"), ("White", "White"),
            ("WhiteTOP", "WhiteTOP"), ("White BEST", "White BEST"),
            ("White VIP", "White VIP"),
            ("Brown Laminet eghtesadi", "Brown Laminet eghtesadi"),
            ("Brown Laminet", "Brown Laminet"), ("Brown TOP Laminet", "Brown TOP Laminet"),
            ("Light White E Laminet eghtesadi", "Light White E Laminet eghtesadi"),
            ("White Laminet eghtesadi", "White Laminet eghtesadi"),
            ("White Laminet", "White Laminet"), ("WhiteTOP Laminet", "WhiteTOP Laminet"),
            ("VIP Laminet", "VIP Laminet")
        ],
        label="ترکیب متریال",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_material_combination'}),
        initial="انتخاب کنید",
        required=False,
    )

    printing = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("flexo", "فلکسو"), ("offset", "افست")
        ],
        label="نوع چاپ",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    sheet_roll = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("sheet", "شیت"), ("roll", "رول")
        ],
        label="شیت/رول",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    coating = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("none", "بدون روکش"), ("mat_thermal", "مات حرارتی"),
            ("mat_water", "مات واتر بیس"), ("glossy_thermal", "براق حرارتی"),
            ("glossy_water", "براق واتر بیس"), ("uv", "UV"), ("varnish", "ورنی")
        ],
        label="روکش",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required=False,
    )

    color_count = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("1", "1 رنگ"), ("2", "2 رنگ"),
            ("3", "3 رنگ"), ("4", "4 رنگ")
        ],
        label="تعداد رنگ",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    joining = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("glue", "چسب"), ("staple", "منگنه"), ("both", "منگنه + چسب")
        ],
        label="اتصال",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required=False,
    )

    group_selection = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("all", "تمام عرض‌ها"), ("main", "عرض‌های اصلی"),
            ("sub1", "عرض‌های فرعی ۱"), ("sub2", "عرض‌های فرعی ۲"),
            ("sub3", "عرض‌های فرعی ۳")
        ],
        label="انتخاب گروه",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    packaging = forms.ChoiceField(
        choices=[
            ("", "انتخاب کنید"),
            ("none", "بدون بسته‌بندی"), ("shrink", "شرینگ"),
            ("pallet", "پالت"), ("pallet_shrink", "پالت و شرینگ")
        ],
        label="بسته‌بندی ارسال",
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial="انتخاب کنید",
        required = False,
    )

    class Meta:
        model = Carton
        fields = '__all__'
        widgets = {
            'order_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'dimension_type': forms.Select(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "model": "مدل کارتن",
            "order_quantity": "تعداد سفارش",
            "length": "طول (سانتی‌متر)",
            "width": "عرض (سانتی‌متر)",
            "height": "ارتفاع (سانتی‌متر)",
            "time": "زمان تحویل",
            "top_color": "رنگ رویه",
            "layer_count": "تعداد لایه",
            "flute": "نوع فلوت",
            "material_combination": "ترکیب متریال",
            "printing": "نوع چاپ",
            "sheet_roll": "شیت/رول",
            "coating": "روکش",
            "color_count": "تعداد رنگ",
            "joining": "روش اتصال",
            "group_selection": "انتخاب گروه",
            "packaging": "بسته‌بندی",
        }

    # ✅ اعتبارسنجی فرم
    def clean(self):
        cleaned_data = super().clean()
        printing = cleaned_data.get("printing")
        sheet_roll = cleaned_data.get("sheet_roll")

        # اگر چاپ "افست" باشد، حتماً باید "شیت یا رول" انتخاب شود
        if printing == "offset" and not sheet_roll:
            self.add_error("sheet_roll", "در صورت انتخاب چاپ افست، نوع شیت یا رول را مشخص کنید.")

        return cleaned_data

class CartonFilterForm(forms.Form):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        required=False,
        label="مشتری",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    model = forms.ChoiceField(
        required=False,
        label="مدل",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    top_color = forms.ChoiceField(
        required=False,
        label="رنگ رویه",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    from_date = forms.DateField(
        required=False,
        label="از تاریخ",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    to_date = forms.DateField(
        required=False,
        label="تا تاریخ",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(CartonFilterForm, self).__init__(*args, **kwargs)

        # مقدار `choices` از دیتابیس پر می‌شود
        self.fields['model'].choices = [("", "انتخاب کنید")] + list(
            Carton.objects.values_list("model", "model").distinct()
        )

        self.fields['top_color'].choices = [("", "انتخاب کنید")] + list(
            Carton.objects.values_list("top_color", "top_color").distinct()
        )