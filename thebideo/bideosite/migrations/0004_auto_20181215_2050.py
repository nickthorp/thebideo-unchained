# Generated by Django 2.1.3 on 2018-12-16 02:50
import csv
from datetime import datetime
from django.db import migrations
from django.utils.timezone import make_aware


def insert_initial_data(apps, schema_editor):
    Podcast = apps.get_model('bideosite', 'Podcast')
    Youtube = apps.get_model('bideosite', 'Youtube')
    with open('bideosite/migrations/bideosite_podcast.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'id':
                _, created = Podcast.objects.get_or_create(
                    # id=row[0],
                    episode_title=row[1],
                    episode_number=row[2],
                    file_url=row[3],
                    pub_date=make_aware(datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S')),
                    episode_desc=row[5],
                    img_url=row[6]
                )
    with open('bideosite/migrations/bideosite_youtube.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'id':
                _, created = Youtube.objects.get_or_create(
                    id=row[0],
                    video_title=row[1],
                    video_url=row[2],
                    video_description=row[3],
                )


class Migration(migrations.Migration):

    dependencies = [
        ('bideosite', '0003_youtube'),
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]
