# Generated by Django 3.0.3 on 2020-07-21 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='published_date',
        ),
    ]
