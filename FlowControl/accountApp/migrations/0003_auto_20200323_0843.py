# Generated by Django 3.0.4 on 2020-03-23 08:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accountApp', '0002_auto_20200321_0306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SfeduStudent',
            new_name='Profile',
        ),
    ]
