# Generated by Django 3.0.3 on 2020-05-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_property_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
