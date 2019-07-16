from django.contrib import admin

from .models import Podcast, Youtube, YoutubeChannel, TwitchUser

# Register your models here.
admin.site.register(Podcast)
admin.site.register(Youtube)
admin.site.register(YoutubeChannel)
admin.site.register(TwitchUser)
