# Generated by Django 4.0.1 on 2022-01-20 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chirp', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='chirp',
        ),
    ]