# Generated by Django 4.0.1 on 2022-01-13 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publish_date', models.DateField()),
                ('checked_out', models.BooleanField(default=True)),
                ('checkout_time', models.DateField()),
                ('author', models.ForeignKey(max_length=25, on_delete=django.db.models.deletion.PROTECT, to='bookshelf.author')),
            ],
        ),
    ]
