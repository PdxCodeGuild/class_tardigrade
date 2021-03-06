# Generated by Django 4.0.1 on 2022-01-21 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checkout', to='library_app.book'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='user',
            field=models.CharField(max_length=75),
        ),
    ]
