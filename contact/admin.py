from .models import Message
from django.contrib import admin

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_date',)
    list_per_page = 10
    list_display_links = ('id',)
    list_editable = ('name', 'email', 'subject', 'message')