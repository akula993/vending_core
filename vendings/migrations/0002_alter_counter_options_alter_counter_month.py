# Generated by Django 4.2 on 2023-04-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='counter',
            options={'verbose_name_plural': 'Счетчики'},
        ),
        migrations.AlterField(
            model_name='counter',
            name='month',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата снятия счетчика'),
        ),
    ]
