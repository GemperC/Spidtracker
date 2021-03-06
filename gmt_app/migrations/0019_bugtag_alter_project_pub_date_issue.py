# Generated by Django 4.0.5 on 2022-06-27 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmt_app', '0018_alter_project_description_alter_project_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('pud_date', models.DateTimeField(blank=True, null=True)),
                ('severity', models.CharField(blank=True, choices=[('enhancment', 'ENHANCMENT'), ('minor', 'MINOR'), ('major', 'MAJOR'), ('critical', 'CRITICAL'), ('blocker', 'BLOCKER')], max_length=15, null=True)),
                ('bug_tags', models.ManyToManyField(blank=True, to='gmt_app.bugtag')),
                ('issue_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_issue_creator', to='gmt_app.user')),
                ('issue_solver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_issue_solver', to='gmt_app.user')),
            ],
        ),
    ]
