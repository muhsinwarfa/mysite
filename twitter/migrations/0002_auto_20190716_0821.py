# Generated by Django 2.2.2 on 2019-07-16 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='time_posted',
        ),
        migrations.AddField(
            model_name='follower',
            name='user_id_1',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='activity',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follower',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follower',
            name='user_id_2',
            field=models.IntegerField(default='2'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='is_reply',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='is_retweet',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='is_tweet',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='like_count',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='original_tweet_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='reply_count',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweet_count',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]