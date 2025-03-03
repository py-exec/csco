from django import forms

class CartonForm(forms.Form):
    model_choices = [
        ("", "انتخاب کنید"),
        ("B01+B", "B01+B"),
        ("D27", "D27"),
        ("B15", "B15"),
        ("B11", "B11"),
        ("B17", "B17"),
        ("B01+D", "B01+D"),
        ("B00", "B00"),
        ("B03", "B03"),
    ]

    order_quantity = forms.IntegerField(
        label="تعداد سفارش",
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "مثلاً 1501"})
    )

    model = forms.ChoiceField(
        choices=model_choices,
        label="مدل",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    dimensions_choices = [
        ("", "انتخاب کنید"),
        ("internal", "داخلی کارتن"),
        ("external", "خارجی کارتن"),
    ]
    dimensions = forms.ChoiceField(
        choices=dimensions_choices,
        label="ابعاد درخواستی",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    length = forms.IntegerField(label="طول", min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
    width = forms.IntegerField(label="عرض", min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
    height = forms.IntegerField(label="ارتفاع", min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}))

    time_choices = [
        ("", "انتخاب کنید"),
        ("1w", "1w"),
        ("2w", "2w"),
        ("4w", "4w"),
        ("shop", "Shop"),
    ]
    time = forms.ChoiceField(choices=time_choices, label="زمان", widget=forms.Select(attrs={"class": "form-select"}))

    top_color_choices = [
        ("", "انتخاب کنید"),
        ("brown", "قهوه‌ای"),
        ("white", "سفید"),
        ("laminate", "لمینت"),
    ]
    top_color = forms.ChoiceField(choices=top_color_choices, label="رنگ رویه", widget=forms.Select(attrs={"class": "form-select"}))

    layer_count_choices = [
        ("", "انتخاب کنید"),
        ("3", "3"),
        ("5", "5"),
    ]
    layer_count = forms.ChoiceField(choices=layer_count_choices, label="تعداد لایه", widget=forms.Select(attrs={"class": "form-select"}))

    flute_choices = [
        ("", "انتخاب کنید"),
        ("B", "B"),
        ("C", "C"),
        ("E", "E"),
        ("BC", "BC"),
        ("EB", "EB"),
        ("EC", "EC"),
    ]
    flute = forms.ChoiceField(choices=flute_choices, label="فلوت", widget=forms.Select(attrs={"class": "form-select"}))

    material_combination = forms.CharField(label="ترکیب متریال", widget=forms.TextInput(attrs={"class": "form-control"}))

    printing_choices = [
        ("", "انتخاب کنید"),
        ("flexo", "فلکسو"),
        ("offset", "افست"),
    ]
    printing = forms.ChoiceField(choices=printing_choices, label="چاپ", widget=forms.Select(attrs={"class": "form-select"}))

    sheet_roll_choices = [
        ("", "انتخاب کنید"),
        ("sheet", "شیت"),
        ("roll", "رول"),
    ]
    sheet_roll = forms.ChoiceField(choices=sheet_roll_choices, label="انتخاب شیت و رول مقوا در لمینتی", widget=forms.Select(attrs={"class": "form-select"}), required=False)

    coating_choices = [
        ("", "انتخاب کنید"),
        ("none", "ندارد"),
        ("mat_thermal", "مات حرارتی"),
        ("mat_water", "مات واتر بیس"),
        ("glossy_thermal", "براق حرارتی"),
        ("glossy_water", "براق واتر بیس"),
        ("uv", "UV"),
        ("varnish", "ورنی"),
    ]
    coating = forms.ChoiceField(choices=coating_choices, label="روکش", widget=forms.Select(attrs={"class": "form-select"}), required=False)

    color_count_choices = [
        ("", "انتخاب کنید"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    ]
    color_count = forms.ChoiceField(choices=color_count_choices, label="تعداد رنگ", widget=forms.Select(attrs={"class": "form-select"}))

    joining_choices = [
        ("", "انتخاب کنید"),
        ("glue", "چسب"),
        ("staple", "منگنه"),
        ("both", "منگنه + چسب"),
    ]
    joining = forms.ChoiceField(choices=joining_choices, label="اتصال", widget=forms.Select(attrs={"class": "form-select"}), required=False)

    group_selection_choices = [
        ("", "انتخاب کنید"),
        ("all", "تمام عرض‌ها"),
        ("main", "عرض‌های اصلی"),
        ("sub1", "عرض‌های فرعی ۱"),
        ("sub2", "عرض‌های فرعی ۲"),
        ("sub3", "عرض‌های فرعی ۳"),
    ]
    group_selection = forms.ChoiceField(choices=group_selection_choices, label="انتخاب گروه", widget=forms.Select(attrs={"class": "form-select"}))

    packaging_choices = [
        ("", "انتخاب کنید"),
        ("none", "بدون بسته‌بندی"),
        ("pallet", "پالت"),
        ("shrink", "شرینگ"),
        ("pallet_shrink", "پالت و شرینگ"),
    ]
    packaging = forms.ChoiceField(choices=packaging_choices, label="بسته‌بندی ارسال", widget=forms.Select(attrs={"class": "form-select"}))