# Generated by Django 3.2.8 on 2021-11-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0014_testmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.IntegerField(max_length=200),
        ),
    ]