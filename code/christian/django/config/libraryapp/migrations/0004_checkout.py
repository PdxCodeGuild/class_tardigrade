# Generated by Django 4.0.1 on 2022-01-13 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_book_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('checkout', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checkouts', to='libraryapp.book')),
            ],
        ),
    ]