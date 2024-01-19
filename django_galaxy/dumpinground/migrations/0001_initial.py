# Generated by Django 4.2.8 on 2023-12-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dump",
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
                ("name", models.CharField(max_length=256, unique=True)),
                ("data", models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
