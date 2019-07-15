from django.contrib import admin

from .models import Podcast, Youtube, YoutubeChannel

# Register your models here.
admin.site.register(Podcast)
admin.site.register(Youtube)
admin.site.register(YoutubeChannel)