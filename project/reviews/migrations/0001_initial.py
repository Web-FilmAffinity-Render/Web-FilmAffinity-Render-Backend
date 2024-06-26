# Generated by Django 5.0.6 on 2024-05-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="review",
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
                ("movie_title", models.CharField(max_length=100)),
                ("user_username", models.EmailField(max_length=254)),
                ("review_text", models.TextField()),
                ("review_rate", models.FloatField(max_length=4)),
            ],
        ),
    ]
