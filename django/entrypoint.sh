#!/bin/sh

python manage.py migrate --noinput --settings umihiko_server_v2.settings.production
python manage.py collectstatic --noinput --clear --settings umihiko_server_v2.settings.production

if [ "$#" -gt 0 ]; then
  $@
fi

uwsgi --ini uwsgi.ini --http 0.0.0.0:$PORT
