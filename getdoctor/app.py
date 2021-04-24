from flask import Flask
from flask_migrate import Migrate
from getdoctor.api import api
from getdoctor.models import db
from  getdoctor import config

import logging
import os


logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()
migrate = Migrate()

def create_app():

   logger.info(f'Starting app in {config.APP_ENV} environment')
   logger.info(f'Debugging = {config.DEBUG}')
   app = Flask(__name__)
   app.config.from_object('getdoctor.config')
   
   api.init_app(app)
   db.init_app(app)
   migrate.init_app(app,db)

   # define hello world page
   @app.route('/')
   def hello_world():
      return 'Hello, World!'

   return app


if __name__ == "__main__":
   app = create_app()
   app.run(host='0.0.0.0', debug=True)
