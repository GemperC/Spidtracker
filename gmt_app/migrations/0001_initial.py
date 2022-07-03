# Generated by Django 4.0.5 on 2022-06-16 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=256)),
                ('pud_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
