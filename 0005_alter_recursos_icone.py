# Generated by Django 4.1.3 on 2022-12-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_cargo_horas_remove_funcionario_horas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recursos',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Laptop'), ('lni-leaf', 'Folha'), ('lni-layers', 'Camadas'), ('lni-mobile', 'Modile'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='icone'),
        ),
    ]
