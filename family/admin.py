from django.contrib import admin
from . import models

# Register your models here.

# 后台管理界面-Menu
@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':['title']
    }
    list_display = ['title','description','chef']

# 后台管理界面-Chef
@admin.register(models.Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name']