from django.db import migrations

def delete_all_migrations(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE django_migrations CASCADE;")

class Migration(migrations.Migration):
    dependencies = []  # No dependencies = runs first
    operations = [
        migrations.RunPython(delete_all_migrations),
    ]
