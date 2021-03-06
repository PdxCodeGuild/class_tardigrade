# Generated by Django 4.0.1 on 2022-01-19 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0003_person_lived_in_states_alter_person_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lived_in_states',
            field=models.ManyToManyField(related_name='one_time_residents', to='census.State'),
        ),
    ]
