# Generated by Django 5.1.1 on 2024-09-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="last_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
