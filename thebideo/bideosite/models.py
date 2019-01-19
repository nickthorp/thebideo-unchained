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


class Youtube(models.Model):
    video_title = models.CharField(max_length=255)
    video_url = models.URLField()
    video_description = models.TextField()
    pub_date = models.DateTimeField('date published', default='2005-02-14 12:00:00')

    def __str__(self):
        return self.video_title
