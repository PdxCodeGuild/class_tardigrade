# Generated by Django 4.0.1 on 2022-01-12 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_rename_user_name_checked_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('checkout', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now=True, verbose_name='checkout time')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='published_date',
            new_name='publish_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='available',
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.author'),
        ),
        migrations.DeleteModel(
            name='Checked',
        ),
        migrations.AddField(
            model_name='genre',
            name='book',
            field=models.ManyToManyField(to='library.Book'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checkouts', to='library.book'),
        ),
    ]