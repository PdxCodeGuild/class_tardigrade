# Generated by Django 4.0.1 on 2022-01-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_checkoutbook_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='checkoutbook',
            name='time_stamp',
            field=models.TimeField(blank=True),
        ),
    ]
