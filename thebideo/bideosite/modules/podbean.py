import feedparser
import string
from datetime import datetime


entry_string = ''
d = feedparser.parse('https://bideo.podbean.com/feed.xml')
for i in d['entries']:
    date = datetime.strptime(i['published'], '%a, %d %b %Y %H:%M:%S %z')

    entry_list = [00, i['title'], i['title'].split(' ')[2].strip(string.punctuation),
                  i['links'][1]['href'], date.strftime('%Y-%m-%d %H:%M:%S'), "\"" + i['subtitle'] + "\""]
    if 'image' in i:
        entry_list.append(i['image']['href'])
    else:
        entry_list.append('null')
    print(",".join(str(i) for i in entry_list))
