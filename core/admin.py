from django.contrib import admin
from core.models import GeneralSetting, ImageSetting, Skill, Experience
# Register your models here.

class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'parameter', 'updated_date', 'created_date')
    search_fields = ('name', 'description', 'parameter')
    list_filter = ('updated_date', 'created_date')

admin.site.register(GeneralSetting, GeneralSettingAdmin)

class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'file', 'updated_date', 'created_date')
    search_fields = ('name', 'description', 'file')
    list_filter = ('updated_date', 'created_date')

admin.site.register(ImageSetting, ImageSettingAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'name', 'percentage', 'updated_date', 'created_date')
    search_fields = ('name', 'percentage')
    list_filter = ('updated_date', 'created_date')

admin.site.register(Skill, SkillAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'job_title', 'job_location', 'start_date', 'end_date', 'updated_date', 'created_date')
    search_fields = ('company_name', 'job_title', 'job_location')
    list_filter = ('updated_date', 'created_date')

admin.site.register(Experience, ExperienceAdmin)
