# Generated by Django 3.1.6 on 2021-04-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210404_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='overall_rating',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
    ]