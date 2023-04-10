# Generated by Django 4.2 on 2023-04-10 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendings', '0002_counter_month'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='counter',
            options={'ordering': ['-month'], 'verbose_name_plural': 'Счетчики'},
        ),
        migrations.AlterField(
            model_name='counter',
            name='machine',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='counter', to='vendings.machine'),
        ),
    ]
