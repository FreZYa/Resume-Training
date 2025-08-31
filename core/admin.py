from django.contrib import admin
from core.models import GeneralSetting
# Register your models here.

class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'parameter', 'updated_date', 'created_date')
    search_fields = ('name', 'description', 'parameter')
    list_filter = ('updated_date', 'created_date')

admin.site.register(GeneralSetting, GeneralSettingAdmin)