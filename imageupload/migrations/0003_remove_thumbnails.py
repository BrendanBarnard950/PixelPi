# Generated by Django 5.1.4 on 2025-01-12 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0002_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecolor',
            name='thumbnail',
        ),
    ]
