# Generated by Django 4.2.1 on 2023-08-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_alter_assetinwork_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetinwork',
            name='begin_work',
            field=models.DateTimeField(blank=True, null=True, verbose_name='начало работы'),
        ),
        migrations.AlterField(
            model_name='assetinwork',
            name='end_work',
            field=models.DateTimeField(blank=True, null=True, verbose_name='конец работы'),
        ),
    ]
