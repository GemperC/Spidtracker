# Generated by Django 4.0.5 on 2022-06-28 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmt_app', '0023_alter_project_issues'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='issues',
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gmt_app.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]