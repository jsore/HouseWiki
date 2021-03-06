# Generated by Django 3.0 on 2019-12-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191223_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.CharField(choices=[('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5 and up', '5 & up')], default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='ranking',
            field=models.CharField(choices=[('dealbreaker (1)', 'Dealbreaker (1)'), ('very important (2)', 'Very Important (2)'), ('important (3)', 'Important (3)'), ('kind of important (4)', 'Kind of Important (4)'), ('almost petty (5)', 'Almost Petty (5)'), ('definitely petty (6)', 'Definitely Petty (6)')], default='kind of important (2)', max_length=25),
        ),
    ]
