# Generated by Django 2.2.2 on 2019-07-16 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20190716_0821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='follower',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='user_id',
            new_name='user',
        ),
    ]
