# Generated by Django 4.0.1 on 2022-01-13 23:22

from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.DateField(default=library.models.return_date_time),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.author'),
        ),
    ]
