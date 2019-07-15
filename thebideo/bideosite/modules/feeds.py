import feedparser
import string
from datetime import datetime
from dateutil.parser import parse
from .. import models


def parse_podbean_feed():
    d = feedparser.parse('https://bideo.podbean.com/feed.xml')
    for i in d['entries']:
        if 'image' in i:
            image = i['image']['href']
        else:
            image = 'https://pbcdn1.podbean.com/imglogo/image-logo/1501784/Purple-13.png'
        try:
            episode_number = float(i['title'].split(' ')[2].strip(string.punctuation))
        except ValueError:
            episode_number = 0.0
        try:
            podcast = models.Podcast.objects.get(episode_title=i['title'],file_url=i['links'][1]['href'])
            podcast.episode_desc = i['subtitle']
            podcast.episode_number = episode_number
            podcast.img_url = image
            podcast.pub_date = datetime.strptime(i['published'], '%a, %d %b %Y %H:%M:%S %z')
            podcast.save()
        except models.Podcast.DoesNotExist:
            models.Podcast.objects.create(
                episode_title=i['title'],
                episode_number=episode_number,
                file_url=i['links'][1]['href'],
                pub_date=datetime.strptime(i['published'], '%a, %d %b %Y %H:%M:%S %z'),
                episode_desc=i['subtitle'],
                img_url=image
            )


def parse_youtube_feeds():
    channels = models.YoutubeChannel.objects.order_by('channel_name')
    print(channels)
    for channel in channels:
        feed_contents = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id={id}"
                                         .format(id=channel.channel_id))
        for i in feed_contents['entries']:
            models.Youtube.objects.create(
                video_title=i['title'],
                video_url="https://www.youtube.com/embed/{vid_id}".format(vid_id=i['yt_videoid']),
                video_description=i['summary'],
                pub_date=parse(i['published']),
                channel=channel
            )
