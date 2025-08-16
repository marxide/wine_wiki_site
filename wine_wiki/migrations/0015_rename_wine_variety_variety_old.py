import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("wine_wiki", "0014_create_fill_variety_model")]

    operations = [
        migrations.RenameField(
            model_name="wine",
            old_name="variety",
            new_name="variety_old",
        ),
    ]
