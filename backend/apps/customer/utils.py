from django.contrib.auth.models import Group, Permission

def user_has_permission(user, permission_name):
    """
    بررسی می‌کند که آیا کاربر دارای یک سطح دسترسی خاص است یا خیر.
    این بررسی را هم در گروه‌ها و هم در مجوزهای مستقیم کاربر انجام می‌دهد.
    """
    if user.is_superuser:  # ادمین همیشه دسترسی دارد
        return True

    return user.has_perm(permission_name) or user.groups.filter(permissions__codename=permission_name).exists()