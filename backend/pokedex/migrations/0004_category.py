# Generated by Django 2.2.7 on 2019-12-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_auto_20191201_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pokemones', models.ManyToManyField(to='pokedex.Pokedex')),
            ],
        ),
    ]
