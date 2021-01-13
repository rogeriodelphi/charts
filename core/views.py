from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import Meses, Curso, Matricula
from django.db.models import Count

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):
    def get_labels(self):
        """Retorna 12 labels para a representação do x (MESES DO ANO)"""
        # meses = Curso.objects.all()
        labels = list(map(str, Curso.objects.values('mes').order_by('id')))
        return labels

    def get_providers(self):
        """Retorna os nomes dos cursos"""
        #cursos = Curso.objects.values('curso')
        # datasets = list(map(str, cursos))
        datasets = Curso.objects.values('curso')
#        print(datasets)
        return list(map(str, datasets))


    def get_data(self):
        total_mes = Curso.objects.count()
        total_cursos = Curso.objects.count()
        print('Total de cursos: ',  total_cursos)
        dados = []
        for l in range(total_cursos):#define os cursos datasets
            for c in range(total_cursos):
                dado = [20, 30, 40, 50, 60, 70]
            dados.append(dado)
        return dados


