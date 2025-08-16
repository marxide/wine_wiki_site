import django.db.models.deletion
from django.db import migrations, models


def populate_variety(apps, schema_editor):
    Wine = apps.get_model("wine_wiki", "Wine")
    Variety = apps.get_model("wine_wiki", "Variety")

    varieties = list(
        Wine.objects.exclude(variety__isnull=True)
        .values_list("variety", flat=True)
        .distinct()
    )

    for name in varieties:
        variety = Variety(name=name)
        try:
            variety.save()
        except Exception as e:
            breakpoint()


def reverse_populate_variety(apps, schema_editor):
    Variety = apps.get_model("wine_wiki", "Variety")

    Variety.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("wine_wiki", "0013_update_wine_variety_set_null_blank"),
    ]

    operations = [
        migrations.CreateModel(
            name="Variety",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RunPython(
            code=populate_variety,
            reverse_code=reverse_populate_variety,
        ),
    ]
