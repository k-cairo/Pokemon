# Generated by Django 4.0.4 on 2022-05-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='img_link',
            field=models.URLField(blank=True),
        ),
    ]