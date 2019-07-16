from datetime import datetime

from django.db import models


# Create your models here.
class Podcast(models.Model):
    episode_title = models.CharField(max_length=255)
    episode_number = models.FloatField()
    file_url = models.URLField()
    img_url = models.URLField()
    pub_date = models.DateTimeField('date published')
    episode_desc = models.TextField()

    def __str__(self):
        return self.episode_title


class YoutubeChannel(models.Model):
    channel_id = models.CharField(max_length=255)
    channel_name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.channel_name


class Youtube(models.Model):
    video_title = models.CharField(max_length=255)
    video_url = models.URLField()
    video_description = models.TextField()
    pub_date = models.DateTimeField('date published', default=datetime.strptime('2005-02-14 12:00:00 +0000', '%Y-%m-%d %H:%M:%S %z'))
    channel = models.ForeignKey(YoutubeChannel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.video_title


class TwitchUser(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    profile_image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name
