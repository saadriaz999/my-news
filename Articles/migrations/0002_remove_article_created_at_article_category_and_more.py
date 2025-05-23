# Generated by Django 5.1.6 on 2025-04-05 01:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Articles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="created_at",
        ),
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.CharField(default="General", max_length=20),
        ),
        migrations.AddField(
            model_name="article",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.CharField(default="Unknown Author", max_length=100),
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(default="No content available."),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(default="Untitled Article", max_length=255),
        ),
    ]
