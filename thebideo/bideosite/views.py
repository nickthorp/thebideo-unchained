import json
import os
import yaml
from django.shortcuts import render
from django.http import HttpResponse

from .models import Podcast, Youtube
from .forms import ContactForm
from .modules.contact import verify_recaptcha, mailgun


# Load up our configuration file
if os.environ['ENV'] == 'PRODUCTION':
    yml_path = os.getcwd() + "/etc/thebideo/config.yml"
else:
    yml_path = os.getcwd() + "/bideosite/config.yml"
with open(yml_path, 'r') as yaml_file:
    cfg = yaml.load(yaml_file)


def index(request):
    context = {
        "podcast": Podcast.objects.order_by('-pub_date')[:1],
        "youtubes": Youtube.objects.order_by('video_title')[:1],
    }
    return render(request, 'bideosite/index.html', context)


def podcast(request):
    podcast_list = Podcast.objects.order_by('-pub_date')
    output = "<br>".join([p.episode_title for p in podcast_list])
    context = {

    }
    return HttpResponse(output)


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
                message = "Success"
            else:
                message = "Robot"
    form = ContactForm()
    context = {'form': form, 'message': message}
    return render(request, 'bideosite/contact.html', context)


def comment(request):
    return HttpResponse(request)
