# Generated by Django 3.2.6 on 2021-10-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_alter_resultados_resultado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultados',
            name='resultado',
            field=models.DecimalField(decimal_places=3, max_digits=50),
        ),
    ]
