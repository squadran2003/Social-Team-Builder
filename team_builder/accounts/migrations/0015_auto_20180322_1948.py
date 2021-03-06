# Generated by Django 2.0.3 on 2018-03-22 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20180321_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(null=True, upload_to='avatars/')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
