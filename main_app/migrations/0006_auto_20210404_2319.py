# Generated by Django 3.1.6 on 2021-04-04 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_truck_overall_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='overall_rating',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
