# Generated by Django 4.0.5 on 2022-06-23 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gmt_app', '0007_remove_project_team_project_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='members',
            new_name='team_members',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='team_name',
        ),
    ]