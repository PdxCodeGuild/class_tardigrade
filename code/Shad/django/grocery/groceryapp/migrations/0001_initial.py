# Generated by Django 4.0.1 on 2022-01-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('completed_date', models.DateField()),
                ('completed', models.BooleanField(default=True)),
            ],
        ),
    ]
