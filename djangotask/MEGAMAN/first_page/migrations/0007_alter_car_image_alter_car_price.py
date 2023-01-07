# Generated by Django 4.1.4 on 2023-01-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_page', '0006_trip_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]