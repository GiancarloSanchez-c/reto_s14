from django.contrib import admin
from .models import Auto
# Register your models here.

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'marca','año','precio']
    search_fields = ['id', 'marca','modelo', 'año','precio']
