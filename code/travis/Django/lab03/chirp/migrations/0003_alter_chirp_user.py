# Generated by Django 4.0.1 on 2022-01-21 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chirp', '0002_remove_chirp_user_name_chirp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
