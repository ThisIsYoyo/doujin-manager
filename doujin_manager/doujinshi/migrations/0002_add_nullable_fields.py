# Generated by Django 4.1.7 on 2023-03-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doujinshi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doujinshi",
            name="buy_way",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name="doujinshi",
            name="origin_language",
            field=models.CharField(
                choices=[(None, ""), ("JAPANESE", "Japanese"), ("CHINESE", "Chinese")],
                default=None,
                max_length=8,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="doujinshi",
            name="present_language",
            field=models.CharField(
                choices=[(None, ""), ("JAPANESE", "Japanese"), ("CHINESE", "Chinese")],
                default=None,
                max_length=8,
                null=True,
            ),
        ),
    ]
