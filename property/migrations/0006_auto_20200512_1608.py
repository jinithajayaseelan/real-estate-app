# Generated by Django 3.0.3 on 2020-05-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_property_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('sale', 'sale'), ('rent', 'rent')], max_length=10),
        ),
    ]
