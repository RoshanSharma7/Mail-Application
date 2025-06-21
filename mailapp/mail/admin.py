from django.contrib import admin
from .models import MailUser

@admin.register(MailUser)
class MailUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'created_at']
