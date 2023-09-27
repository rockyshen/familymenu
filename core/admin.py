from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (          # 在admin管理后台，定义在创建新用户时要显示在管理界面的字段集合及外观
        (
            None,              # 字段集合的标题
            {
                "classes": ("wide",),   # 字段集合展示的样式
                "fields": ("username", "password1",'password2',"email"),
            },
        ),
    )