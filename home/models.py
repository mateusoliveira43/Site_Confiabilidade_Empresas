from django.db import models
from django.db.models import Count

# Create your models here.


class ConfiabilidadeEmpresa(models.Model):
    nome = models.CharField(max_length=150)
    logo = models.ImageField(blank=True, upload_to='logos')
    descricao = models.TextField(blank=True)
    indice = models.PositiveIntegerField(default=50)

    def ranking(self):
        aggregate = ConfiabilidadeEmpresa.objects.filter(
            indice__gt=self.indice).aggregate(ranking=Count('indice'))
        return aggregate['ranking'] + 1

    def __str__(self):
        return self.nome

    def processar_financas(self):
        return None
