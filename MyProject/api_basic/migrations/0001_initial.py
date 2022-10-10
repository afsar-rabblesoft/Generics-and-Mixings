# Generated by Django 4.1.1 on 2022-10-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
