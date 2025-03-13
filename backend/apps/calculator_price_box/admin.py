from django.contrib import admin
from .models import (
    WidthSelection, DimensionConversionB01B,Carton
)

# ثبت مدل‌ها در پنل ادمین
admin.site.register(WidthSelection)
admin.site.register(DimensionConversionB01B)
admin.site.register(Carton)
