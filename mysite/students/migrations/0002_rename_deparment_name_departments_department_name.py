# Generated by Django 4.0.6 on 2022-07-21 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='deparment_name',
            new_name='department_name',
        ),
    ]
