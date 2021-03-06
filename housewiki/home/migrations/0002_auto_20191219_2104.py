# Generated by Django 3.0 on 2019-12-19 21:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='ranking',
            field=models.CharField(choices=[('dealbreaker', 'Dealbreaker'), ('very important', 'Very Important'), ('important', 'Important'), ('kind of important', 'Kind of Important'), ('almost petty', 'Almost Petty'), ('definitely petty', 'Definitely Petty')], default='kind of important', max_length=20),
        ),
    ]
