# Generated by Django 4.0.1 on 2022-01-17 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_is_checked_out'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('checkout', models.CharField(max_length=30)),
                ('time_stamp', models.CharField(max_length=30)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]
