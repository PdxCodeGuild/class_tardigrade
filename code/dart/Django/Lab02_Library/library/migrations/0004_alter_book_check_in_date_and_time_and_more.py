# Generated by Django 4.0.1 on 2022-01-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rename_name_book_title_remove_author_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='check_in_date_and_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='check_out_date_and_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
