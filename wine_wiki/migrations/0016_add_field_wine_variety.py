import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wine_wiki", "0015_rename_wine_variety_variety_old"),
    ]

    operations = [
        migrations.AddField(
            model_name="wine",
            name="variety",
            field=models.CharField(default=""),
        ),
    ]
