# Generated by Django 4.0.1 on 2022-01-19 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_checkout_genre_remove_book_checked_out_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
    ]