# Generated by Django 2.0.3 on 2018-04-24 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_applied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='applied',
        ),
        migrations.AddField(
            model_name='position',
            name='applied',
            field=models.BooleanField(default=False),
        ),
    ]