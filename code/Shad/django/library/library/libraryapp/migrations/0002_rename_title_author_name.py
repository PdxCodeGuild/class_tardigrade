# Generated by Django 4.0.1 on 2022-01-13 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='title',
            new_name='name',
        ),
    ]
