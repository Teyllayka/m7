# Generated by Django 5.0.4 on 2025-04-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0011_remove_pages_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="pages",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
