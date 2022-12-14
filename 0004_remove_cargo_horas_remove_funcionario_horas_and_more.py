# Generated by Django 4.1.3 on 2022-12-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cargo_horas_funcionario_horas_recursos_horas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='horas',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='horas',
        ),
        migrations.RemoveField(
            model_name='recursos',
            name='horas',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='horas',
        ),
        migrations.AlterField(
            model_name='cargo',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='recursos',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualização'),
        ),
    ]
