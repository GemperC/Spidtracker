# Generated by Django 4.0.5 on 2022-06-28 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmt_app', '0031_alter_issue_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gmt_app.project'),
        ),
    ]
