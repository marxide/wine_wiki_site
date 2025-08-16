import django.db.models.deletion
from django.db import migrations, models


def fill_null_with_blank(apps, schema_editor):
    Wine = apps.get_model("wine_wiki", "wine")

    for wine in Wine.objects.all():
        if not wine.variety:
            wine.variety = ""
            wine.save()


def reverse_fill_null_with_blank(apps, schema_editor):
    Wine = apps.get_model("wine_wiki", "wine")

    for wine in Wine.objects.all():
        if wine.variety == "":
            wine.variety = None
            wine.save()


class Migration(migrations.Migration):
    dependencies = [
        ("wine_wiki", "0012_remove_wine_producer_name"),
    ]

    operations = [
        migrations.RunPython(
            code=fill_null_with_blank, reverse_code=reverse_fill_null_with_blank
        ),
    ]
