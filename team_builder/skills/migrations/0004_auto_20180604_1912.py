# Generated by Django 2.0.3 on 2018-06-04 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20180604_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='user',
            new_name='users',
        ),
    ]