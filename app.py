#!engine/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
from elasticsearch import Elasticsearch
from flask_httpauth import HTTPBasicAuth
import pdb

app = Flask(__name__)
auth = HTTPBasicAuth()
es = Elasticsearch();

# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# @auth.login_required
# def get_tasks():
#     return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/entities/', methods=['GET'])
def get_task():
    result = es.search(index = 'document', q = request.args.get('q'))
    if (not result):
        abort(404)
    return jsonify({'return': result})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/entities/', methods=['POST'])
def create_task():
    #pdb.set_trace()
    newId = actualCount = 0
    try:
        if es.search(index='document', q=''):
            actualCount = es.count(index='document').get('count')
    except:
        actualCount=0
    newId = actualCount+1
    newDocument = es.index(index='document', doc_type=request.json.get('type'), id = newId, body={
        'title': request.json.get('title'),
        'type': request.json.get('type')
    })
    if not newDocument:
        abort(404)
    return jsonify({'newDocument': newDocument}), 201
    #return  201

# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     if not request.json:
#         abort(400)
#     if 'title' in request.json and type(request.json['title']) != unicode:
#         abort(400)
#     if 'description' in request.json and type(request.json['description']) is not unicode:
#         abort(400)
#     if 'done' in request.json and type(request.json['done']) is not bool:
#         abort(400)
#     task[0]['title'] = request.json.get('title', task[0]['title'])
#     task[0]['description'] = request.json.get('description', task[0]['description'])
#     task[0]['done'] = request.json.get('done', task[0]['done'])
#     return jsonify({'task': task[0]})
#
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     tasks.remove(task[0])
#     return jsonify({'result': True})
#
# def make_public_task(task):
#     new_task = {}
#     for field in task:
#         if field == 'id':
#             new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
#         else:
#             new_task[field] = task[field]
#     return new_task
#
# @auth.get_password
# def get_password(username):
#     if username == 'fernando':
#         return 'python'
#     return None
#
# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Acesso nao autorizado'}), 403)

if __name__ == '__main__':
    app.run(debug=True)
