# Generated by Django 2.0.7 on 2018-07-20 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0004_auto_20180720_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]