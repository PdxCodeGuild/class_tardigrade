# Generated by Django 4.0.1 on 2022-01-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_checked_remove_genre_book_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checked',
            options={'verbose_name_plural': 'checks'},
        ),
        migrations.AlterField(
            model_name='checked',
            name='out_date',
            field=models.DateField(default='2022-01-18'),
        ),
    ]