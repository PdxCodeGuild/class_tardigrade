# Generated by Django 4.0.3 on 2022-03-25 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_posts_body_alter_posts_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='user',
            new_name='author',
        ),
    ]
