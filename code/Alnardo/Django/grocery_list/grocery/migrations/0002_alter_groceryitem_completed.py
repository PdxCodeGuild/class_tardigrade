# Generated by Django 4.0.1 on 2022-01-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]