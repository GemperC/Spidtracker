# Generated by Django 4.0.5 on 2022-06-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmt_app', '0015_alter_project_description_alter_project_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=40),
        ),
    ]
