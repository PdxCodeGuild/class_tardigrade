# Generated by Django 4.0.1 on 2022-01-06 19:17

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
                ('description', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=True)),
            ],
        ),
    ]