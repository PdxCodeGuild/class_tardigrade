# Generated by Django 4.0.1 on 2022-01-14 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_return_date_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_Out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('checked_out', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='check_outs', to='library.book')),
            ],
        ),
    ]
