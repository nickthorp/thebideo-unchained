import json
import os
import yaml
import logging
from django.shortcuts import render
from django.http import HttpResponse

from .models import Podcast, Youtube
from .forms import ContactForm
from .modules.contact import verify_recaptcha, mailgun
from .modules.feeds import parse_podbean_feed, parse_youtube_feeds


# Load up our configuration file
try:
    if os.environ['ENV'] == 'PRODUCTION':
        yml_path = "/etc/thebideo/config.yml"
    else:
        yml_path = os.getcwd() + "/bideosite/config.yml"
    with open(yml_path, 'r') as yaml_file:
        cfg = yaml.load(yaml_file)
except KeyError:
    print("Environment Variable doesn't exist. Using defaults")
    pass


logger = logging.getLogger('django')


def index(request):
    context = {
        "podcast": Podcast.objects.order_by('-pub_date')[:1],
        "youtubes": Youtube.objects.exclude(video_title__icontains='The Bideo').order_by('-pub_date')[:1],
    }
    return render(request, 'bideosite/index.html', context)


def podcast(request):
    context = {
        "podcast": Podcast.objects.order_by('-pub_date'),
    }
    return render(request, 'bideosite/podcast.html', context)


def contact(request):
    message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            is_okay = json.loads(verify_recaptcha(form.data['g-recaptcha-response']))
            if is_okay["success"]:
                r = mailgun(form.cleaned_data["email"], cfg['email::to'],
                            form.cleaned_data["subject"], form.cleaned_data["message"])
                if r == "failed":
                    message = "There was a problem."
                else:
                    message = "Success"
            else:
                message = "Robot"
    form = ContactForm()
    context = {'form': form, 'message': message}
    return render(request, 'bideosite/contact.html', context)


def reviews(request):
    context = {
        "youtubes": Youtube.objects.exclude(video_title__startswith='The Bideo').order_by('-pub_date'),
    }
    return render(request, 'bideosite/reviews.html', context)


def healthz(request):
    # logger.debug("Yooo")
    return HttpResponse('Buzz')


def update_podcasts(request):
    parse_podbean_feed()
    parse_youtube_feeds()
    return HttpResponse('We updated our podcasts!')
