# Generated by Django 2.0.3 on 2018-04-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20180422_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='applied',
            field=models.BooleanField(default=False),
        ),
    ]
