# Generated by Django 3.0.3 on 2020-05-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_property_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
    ]
