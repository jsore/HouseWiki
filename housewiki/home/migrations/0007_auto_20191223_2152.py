# Generated by Django 3.0 on 2019-12-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191223_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]
