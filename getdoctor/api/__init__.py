import time
from flask import jsonify
from flask_restful import Api, Resource
from getdoctor.tasks import celery
from getdoctor import config 
from getdoctor.models import db
from getdoctor.models import Department

api = Api(prefix=config.API_PREFIX)

class TaskStatusAPI(Resource):
   def get(self, task_id):
       task = celery.AsyncResult(task_id)
       return jsonify(task.result)


class DataProcessingAPI(Resource):
   def post(self):
       task = process_data.delay()
       return {'task_id': task.id}, 200

class DepatrmentsAPI(Resource):
   def get(self, language, category):
      departments = db.session.query(Department).filter(Department.language == language, Depatrment.category == category).all()

      return jsonify(departments)

class DepartmentAPI(Resource):
   def get(self, id):
      department = db.session.query(Department)


@celery.task()
def process_data():
   time.sleep(60)
   return { 'success': True, 'data': "OK"  }


# data processing endpoint
api.add_resource(DataProcessingAPI, '/process_data')

# task status endpoint
api.add_resource(TaskStatusAPI, '/tasks/<string:task_id>')

api.add_resource(DepatrmentsAPI, 'departments/<string:language>/<string:category>')
api.add_resource(DepartmentAPI, 'department/<string:id>')