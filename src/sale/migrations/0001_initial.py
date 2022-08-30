# Generated by Django 4.1 on 2022-08-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="sale",
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
                ("product_name", models.CharField(max_length=100)),
                ("product_description", models.TextField(max_length=300)),
                ("product_discount", models.CharField(max_length=10)),
                (
                    "product_price",
                    models.DecimalField(decimal_places=2, max_digits=100000),
                ),
            ],
        ),
    ]
