from django.contrib import admin
from .models import Meses, Curso, Matricula

@admin.register(Meses)
class MesAdmin(admin.ModelAdmin):
    list_display = ('id', 'mes', 'obs')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso', 'quantidade', 'mes']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'curso', 'quantidade']