# Generated by Django 4.2 on 2023-06-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smssender', '0003_remove_alarmreport_effect_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmreport',
            name='influence',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]