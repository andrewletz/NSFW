#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import request
from flask import url_for
from flask_cors import CORS

from ModelAPI import *

app = Flask(__name__)
CORS(app)

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/clickbait', methods=['POST'])
def clickbait():
    if not request.json:
        abort(400)
    x = process_and_predict_clickbait_data("Top 100 life hacks for fun style!")
    print(x)
    resp = jsonify({'result': 1})
    resp.headers['Access-Control-Allow-Headers'] = "*"
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = ["GET", "POST", "DELETE", "PUT"]
    return resp, 201

@app.route('/cb', methods=['GET'])
def cb():
    x = process_and_predict_clickbait_data("Top 100 life hacks for fun style!")
    resp = jsonify({'result': x})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    resp = jsonify({'tasks': [make_public_task(task) for task in tasks]})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    resp = jsonify({'task': task[0]})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    if len(task) == 0:
        abort(404)
    return resp

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)