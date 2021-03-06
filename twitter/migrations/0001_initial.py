# Generated by Django 2.2.2 on 2019-06-27 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('activity_name', models.CharField(max_length=50)),
                ('user_id_2', models.IntegerField()),
                ('date_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_id_2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('tweet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.CharField(max_length=150)),
                ('time_posted', models.DateField()),
                ('is_retweet', models.IntegerField()),
                ('is_tweet', models.IntegerField()),
                ('is_reply', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('retweet_count', models.IntegerField()),
                ('reply_count', models.IntegerField()),
                ('original_tweet_id', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
