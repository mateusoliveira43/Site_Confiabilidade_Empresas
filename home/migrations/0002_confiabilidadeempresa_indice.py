# Generated by Django 3.0.7 on 2020-06-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confiabilidadeempresa',
            name='indice',
            field=models.PositiveIntegerField(default=50),
        ),
    ]
