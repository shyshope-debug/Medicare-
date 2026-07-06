from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@medicare.com', 'Medicare2026!')

class Migration(migrations.Migration):
    dependencies = [
        ('pharmacy', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_superuser),
    ]
