import django.db.models.deletion
from django.db import migrations, models
from textwrap import dedent


class Migration(migrations.Migration):
    dependencies = [
        ("wine_wiki", "0016_add_field_wine_variety"),
    ]

    operations = [
        migrations.RunSQL(
            sql=dedent("""
                update
                    wine_wiki_wine
                set
                    variety = b.id
                from
                    wine_wiki_variety b
                where
                    wine_wiki_wine.variety_old = b.name;
            """),
            reverse_sql=dedent("""
            update
                wine_wiki_wine
            set
                variety = '';
                """),
        ),
    ]
