from .models import WidthSelection
import pandas as pd

class WidthOptimizer:
    """کلاس برای محاسبه بهترین عرض ورق بر اساس کمترین میزان پرت"""

    def __init__(self, layer_count, user_defined_width, requested_group):
        """
        مقداردهی اولیه متغیرهای کلاس
        """
        self.layer_count = int(layer_count)
        self.user_defined_width = float(user_defined_width)
        self.requested_group = requested_group.strip()
        self.processed_data = []

    def fetch_available_sheets(self):
        """
        دریافت ورق‌های موجود از دیتابیس بر اساس گروه انتخابی
        """
        available_sheets = WidthSelection.objects.filter(group_name=self.requested_group, available=True)
        if not available_sheets.exists():
            return None
        return available_sheets

    def process_sheets(self, available_sheets):
        """
        پردازش اطلاعات برای محاسبه میزان پرت و انتخاب بهینه‌ترین ورق
        """
        for sheet in available_sheets:
            width = sheet.width_value
            pieces_fit = width // self.user_defined_width
            waste = width % self.user_defined_width
            width_deduction = 3  # مقدار پیش‌فرض کاهش عرض ورق

            self.processed_data.append({
                "group_name": sheet.group_name,
                "sheet_width": width,
                "pieces_fit": pieces_fit,
                "waste": waste,
                "waste_decimal": waste / self.user_defined_width,  # محاسبه میزان پرت اعشاری
                "width_deduction": width_deduction
            })

    def find_best_choice(self):
        """
        یافتن بهترین گزینه با کمترین میزان پرت
        """
        if not self.processed_data:
            return None

        df_results = pd.DataFrame(self.processed_data)
        best_choice = df_results.loc[df_results["waste"].idxmin()]

        return {
            "waste_decimal": round(best_choice["waste_decimal"], 4),
            "waste_integer": int(best_choice["waste"]),
            "selected_width": int(best_choice["sheet_width"]),
            "width_deduction": int(best_choice["width_deduction"])
        }, df_results, best_choice

    def get_results(self):
        """
        اجرای فرآیند محاسبه و ارائه نتایج
        """
        available_sheets = self.fetch_available_sheets()
        if not available_sheets:
            return {"status": "error", "message": f"هیچ ورقی در گروه {self.requested_group} موجود نیست!"}

        self.process_sheets(available_sheets)
        best_choice, df_results, best_choice_df = self.find_best_choice()

        if not best_choice:
            return {"status": "error", "message": "محاسبات انجام نشد، داده‌ای موجود نیست!"}

        return {"status": "success", "data": best_choice}