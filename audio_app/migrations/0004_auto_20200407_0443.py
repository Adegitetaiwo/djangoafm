# Generated by Django 3.0.3 on 2020-04-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_app', '0003_auto_20200407_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audios',
            name='listeners',
            field=models.IntegerField(blank=True),
        ),
    ]
