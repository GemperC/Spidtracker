# Generated by Django 4.0.5 on 2022-06-23 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmt_app', '0006_remove_project_team_project_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gmt_app.team'),
        ),
    ]
