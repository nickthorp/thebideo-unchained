# Generated by Django 2.1.3 on 2018-12-16 02:50
import csv
from django.db import migrations


def insert_initial_data(apps, schema_editor):
    Youtube = apps.get_model('bideosite', 'Youtube')

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
