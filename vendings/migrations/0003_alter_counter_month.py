# Generated by Django 4.2 on 2023-04-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendings', '0002_alter_counter_options_alter_counter_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='month',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата снятия счетчика'),
        ),
    ]
