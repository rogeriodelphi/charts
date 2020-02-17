from django.contrib import admin
from .models import Meses

@admin.register(Meses)
class MesAdmin(admin.ModelAdmin):
    list_display = ('mes',)