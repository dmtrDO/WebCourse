# Generated by Django 5.2 on 2025-04-11 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("length", models.IntegerField()),
                ("isNumbers", models.BooleanField()),
                ("isLetters", models.BooleanField()),
                ("isSpecial", models.BooleanField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.user"
                    ),
                ),
            ],
        ),
    ]
