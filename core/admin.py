from django.contrib import admin
from .models import Meses, Curso

@admin.register(Meses)
class MesAdmin(admin.ModelAdmin):
    list_display = ('mes',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['curso']