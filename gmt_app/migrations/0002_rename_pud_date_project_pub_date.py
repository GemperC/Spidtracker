# Generated by Django 4.0.5 on 2022-06-16 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gmt_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]
