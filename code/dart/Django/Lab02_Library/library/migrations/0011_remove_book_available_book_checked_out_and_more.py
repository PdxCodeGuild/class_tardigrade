# Generated by Django 4.0.1 on 2022-01-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_checked_checked_out_alter_checked_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='available',
        ),
        migrations.AddField(
            model_name='book',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='checked',
            name='check_out_date',
            field=models.DateField(default='2022-01-19'),
        ),
    ]
