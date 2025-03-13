from .models import DimensionConversionB01B
import pandas as pd
from dataclasses import dataclass

@dataclass
class CartonCalculator:
    """کلاس محاسبه گسترده کارتن B01+1"""

    length: float
    width: float
    height: float
    layer_count: int
    flute_type: str
    input_type: str = "خارجی"

    def fetch_conversion_data(self):
        """دریافت داده‌های تبدیل ابعاد و مقادیر لبه چسب از مدل `DimensionConversionB01B`"""
        try:
            conversion = DimensionConversionB01B.objects.get(flute__flute_type=self.flute_type, layer_count=self.layer_count)
            return {
                "length_internal_external": conversion.length_internal_external,
                "width_internal_external": conversion.width_internal_external,
                "height_internal_external": conversion.height_internal_external,
                "glue_flap": conversion.glue_flap,  # دریافت مقدار چسب از دیتابیس
                "flap_tolerance": conversion.flap_tolerance  # دریافت مقدار تلورانس فلاپ از دیتابیس
            }
        except DimensionConversionB01B.DoesNotExist:
            return {"status": "error", "message": f"نوع فلوت `{self.flute_type}` یا تعداد لایه `{self.layer_count}` نامعتبر است!"}

    def convert_dimensions(self, conversion_data):
        """تبدیل ابعاد داخلی به خارجی (در صورت نیاز)"""
        if self.input_type.strip() == "داخلی":
            self.length += conversion_data["length_internal_external"]
            self.width += conversion_data["width_internal_external"]
            self.height += conversion_data["height_internal_external"]

    def calculate_carton_sheet(self, conversion_data):
        """محاسبه گسترده کارتن B01+1"""
        L_sheet = 2 * (self.length + self.width) + conversion_data["glue_flap"]
        W_sheet = self.height + self.width + conversion_data["flap_tolerance"]
        return round(L_sheet, 2), round(W_sheet, 2)

    def get_results(self):
        """اجرای فرآیند محاسبه و ارائه نتایج"""

        # دریافت داده‌های تبدیل و مقادیر چسب از دیتابیس
        conversion_data = self.fetch_conversion_data()
        if "status" in conversion_data and conversion_data["status"] == "error":
            return conversion_data  # بازگشت پیام خطا در صورت عدم وجود داده در دیتابیس

        # تبدیل ابعاد داخلی به خارجی در صورت نیاز
        self.convert_dimensions(conversion_data)

        # محاسبه گسترده کارتن
        L_sheet, W_sheet = self.calculate_carton_sheet(conversion_data)

        # نمایش نتایج در جدول
        df_results = pd.DataFrame([{
            "ابعاد خارجی کارتن (L,W,H)": f"({round(self.length, 2)}, {round(self.width, 2)}, {round(self.height, 2)})",
            "ابعاد گسترده کارتن (L_sheet, W_sheet)": f"({L_sheet}, {W_sheet})"
        }])

        return {
            "status": "success",
            "data": {
                "external_dimensions": (round(self.length, 2), round(self.width, 2), round(self.height, 2)),
                "carton_sheet_dimensions": (L_sheet, W_sheet),
                "glue_flap": conversion_data["glue_flap"],
                "flap_tolerance": conversion_data["flap_tolerance"]
            }
        }