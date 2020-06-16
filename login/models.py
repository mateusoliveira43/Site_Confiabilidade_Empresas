from django.db import models
from home.models import ConfiabilidadeEmpresa
from django import forms
from django.forms.widgets import TextInput, Textarea, FileInput

# Create your models here.


class FormConfiabilidadeEmpresa(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = ConfiabilidadeEmpresa
        exclude = ('indice',)
        labels = {
            'nome': 'Nome da empresa',
            'descricao': 'Descrição',
        }
        widgets = {
            'nome': TextInput(attrs={
                'placeholder': 'Digite o nome da empresa',
                'class': 'form-control',
            }),
            'descricao': Textarea(attrs={
                'placeholder': 'Digite a descrição da empresa (opcional)',
                'class': 'form-control',
                'rows': 5,
            }),
            'logo': FileInput(attrs={
                'placeholder': 'Selecione o logo da empresa (opcional)',
                'class': 'form-control-file',
            }),
        }
