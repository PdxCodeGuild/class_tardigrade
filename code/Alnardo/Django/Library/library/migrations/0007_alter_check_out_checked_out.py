# Generated by Django 4.0.1 on 2022-01-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_remove_book_checked_out_remove_book_return_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_out',
            name='checked_out',
            field=models.BooleanField(default=True),
        ),
    ]
