# Generated by Django 3.0.3 on 2020-04-07 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audios',
            name='date',
            field=models.DateField(blank=True, verbose_name='Date and Time'),
        ),
    ]
