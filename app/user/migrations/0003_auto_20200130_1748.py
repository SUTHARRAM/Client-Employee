# Generated by Django 2.1.15 on 2020-01-30 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200130_1748'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='elient',
            new_name='client',
        ),
    ]
