from django.shortcuts import redirect
from django.conf import settings
import re

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]  # مسیر لاگین باید بدون نیاز به ورود در دسترس باشد

class LoginRequiredMiddleware:
    """
    اطمینان از اینکه همه کاربران قبل از مشاهده صفحات، وارد سیستم شده‌اند.
    فقط مسیرهای مشخص شده در `EXEMPT_URLS` (مثلاً صفحه لاگین) مجاز هستند.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:  # اگر کاربر وارد نشده باشد
            path = request.path_info.lstrip('/')
            if not any(url.match(path) for url in EXEMPT_URLS):  # بررسی استثناء‌ها (مثلاً صفحه لاگین)
                return redirect(settings.LOGIN_URL)  # کاربر را به صفحه لاگین هدایت کن
        return self.get_response(request)