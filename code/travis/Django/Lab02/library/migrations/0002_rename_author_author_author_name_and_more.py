# Generated by Django 4.0.1 on 2022-01-12 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='author_name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_name',
        ),
    ]
