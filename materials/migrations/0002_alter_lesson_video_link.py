# Generated by Django 4.2.2 on 2024-07-20 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="video_link",
            field=models.URLField(
                blank=True, null=True, verbose_name="Ссылка на видео"
            ),
        ),
    ]
