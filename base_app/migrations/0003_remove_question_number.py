# Generated by Django 3.1.1 on 2020-09-23 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_auto_20200923_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='number',
        ),
    ]