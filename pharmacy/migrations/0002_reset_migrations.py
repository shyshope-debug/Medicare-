from django.db import migrations

def delete_ghost_migrations(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("DELETE FROM django_migrations WHERE app = 'pharmacy';")

class Migration(migrations.Migration):
    dependencies = [
        ('pharmacy', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(delete_ghost_migrations),
    ]
