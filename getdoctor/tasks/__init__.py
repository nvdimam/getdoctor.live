from celery import Celery
import getdoctor.config


def make_celery():
   celery = Celery(__name__, broker=getdoctor.config.CELERY_BROKER, include=["getdoctor.api"])
   celery.conf.update(getdoctor.config.as_dict())
   return celery


celery = make_celery()