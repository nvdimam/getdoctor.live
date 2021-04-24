FROM python:3.7.2

RUN pip install pipenv

ADD . /getdoctor.live

WORKDIR /getdoctor.live

RUN pipenv install --system --skip-lock

RUN pip install gunicorn[gevent]

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 getdoctor.wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info