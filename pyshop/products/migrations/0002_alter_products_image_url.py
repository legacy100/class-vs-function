# Generated by Django 4.1 on 2022-08-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="image_url",
            field=models.CharField(max_length=2083, null=True),
        ),
    ]