from django.db import models


# Create your models here.
class Podcast(models.Model):
    episode_title = models.CharField(max_length=255)
    episode_number = models.IntegerField()
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

    def __str__(self):
        return self.video_title
