from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.customer.views import dashboard

urlpatterns = [
    # مسیر پنل مدیریت جنگو
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),

    # مسیرهای عمومی که نیازی به لاگین ندارند
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # مسیرهای اپلیکیشن‌های مختلف (تنها برای کاربران لاگین‌شده)
    # path('', include('apps.core.urls')),
    path('customers/', include('apps.customer.urls')),

    # carton
    path("calculator/", include("apps.calculator_price_box.urls")),  # مسیر صحیح اپلیکیشن
]
