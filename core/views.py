from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import Meses, Curso

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):
    def get_labels(self):
        meses = Meses.objects.all()
        labels = list(map(str, meses))

        """Retorna 12 labels para a representação do x"""
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets"""
        cursos = Curso.objects.all()
        datasets = list(map(str, cursos))

        return datasets

    def get_data(self):
        """Retorna 6 datasets paraplotar o gráfico
        Cada linha representa dataset Y
        Cada coluna representa um label X

        A quantidade de dados precisa ser igual aos dataserts/labels

        12 labels, então 12 colunas
        6 datasets, então 6 linhas
        """

        dados =[]
        for l in range(6):
            for c in range(12):
                dado = [
                    randint(1, 100),  # jan
                    randint(1, 100),  # Fev
                    randint(1, 100),  # Mar
                    randint(1, 100),  # Abr
                    randint(1, 100),  # Mai
                    randint(1, 100),  # jun
                    randint(1, 100),  # jul
                    randint(1, 100),  # Ago
                    randint(1, 100),  # Set
                    randint(1, 100),  # Out
                    randint(1, 100),  # Nov
                    randint(1, 100)  # Dez
                ]
            dados.append(dado)
        return dados
