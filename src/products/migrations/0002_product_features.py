# Generated by Django 4.1 on 2022-08-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="features",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
