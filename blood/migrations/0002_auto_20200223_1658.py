# Generated by Django 2.1 on 2020-02-23 16:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blood', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='blood_donor',
        ),
    ]
