# Generated by Django 4.0.5 on 2022-07-02 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miasta', '0003_place_city_places'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='places',
        ),
        migrations.AddField(
            model_name='place',
            name='place_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='miasta.city'),
        ),
    ]
