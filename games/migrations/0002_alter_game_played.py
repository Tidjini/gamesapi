# Generated by Django 4.1.7 on 2023-02-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="played",
            field=models.BooleanField(default=False),
        ),
    ]