# Generated by Django 3.1.1 on 2020-09-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_auto_20200924_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
