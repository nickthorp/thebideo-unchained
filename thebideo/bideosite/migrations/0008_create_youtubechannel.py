# Generated by Django 2.1.3 on 2019-07-14 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bideosite', '0007_youtube_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeChannel',
            fields=[
                ('channel_id', models.CharField(max_length=255)),
                ('channel_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='youtube',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bideosite.YoutubeChannel'),
        ),
    ]
