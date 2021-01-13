from django.db import models

# Create your models here.

class Meses(models.Model):
    mes = models.CharField(max_length=10, null=False)
    obs = models.TextField

    class Meta:
        verbose_name: 'Mês'
        verbose_name_plural: 'Meses'
        ordering = ('id', 'mes')
        db_table = 'Meses'

    def __str__(self):
        return self.mes

class Curso(models.Model):
    curso = models.CharField(max_length=60, null=False)
    quantidade = models.CharField(max_length=3, null=False)
    mes = models.CharField(max_length=10, null=False)
    obs = models.TextField

    class Meta:
        verbose_name: 'Curso'
        verbose_name_plural: 'Cursos'
        ordering = ['curso']
        db_table = 'Curso'

    def __str__(self):
        return self.curso


class Matricula(models.Model):
    codigo = models.CharField('Código', null=False, max_length=5)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')
    obs = models.TextField

    class Meta:
        verbose_name: 'Matrícula'
        verbose_name_plural: 'Matrículas'
        ordering = ['curso']
        db_table = 'Matricula'

    def __str__(self):
        return self.curso



