# Generated by Django 4.0.1 on 2022-01-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0002_rename_description_groceryitem_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
