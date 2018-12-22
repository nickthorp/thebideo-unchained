FROM python:3

WORKDIR /opt/thebideo-unchained

COPY requirements.txt ./
RUN pip install virtualenv
RUN python -m virtualenv venv
RUN . venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uwsgi

COPY . .

WORKDIR /opt/thebideo-unchained/thebideo
RUN python manage.py collectstatic
RUN ls -al static/bideosite/
EXPOSE 9000
EXPOSE 9191
CMD [ "uwsgi", "wsgi.ini" ]
