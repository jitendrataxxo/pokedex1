# Generated by Django 2.2.7 on 2019-11-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_auto_20191130_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokedex',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
