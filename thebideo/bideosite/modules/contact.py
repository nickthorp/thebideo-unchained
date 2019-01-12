import yaml
import requests
import json
import os

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


def verify_recaptcha(recaptcha_response):
    check_dict = {"secret": cfg['recaptcha::secret'], "response": recaptcha_response}
    r = requests.post(cfg['recaptcha::url'], data=check_dict)
    return r.text


def mailgun(from_who, to_email, subject, text):
    our_email = cfg['mailgun::from']
    user = cfg['mailgun::user']
    password = cfg['mailgun::secret']
    url = cfg['mailgun::url']
    full_text = text + "\n\n" + from_who
    email = {"from": our_email,
             "to": to_email,
             "subject": subject,
             "text": full_text}
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }
    s = requests.Session()
    s.auth = (user, password)
    r = s.post(url, data=email, headers=headers)
    if r.status_code != 200:
        return "failed"
    print(r.status_code)
    print(r.text)
    message = json.loads(r.text)
    print(message["message"])
    return message["message"]
