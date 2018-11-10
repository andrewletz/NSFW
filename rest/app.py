#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import request
from flask import url_for
from flask_cors import CORS

from ModelAPI import *

from VideoData import get_video_data


TruthTable = [True, True, True, True, True, True, True]

MUSIC = 10
CLASSIFY_SET = set([26, 27, 28])


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

# checks if a item should be blurred
@app.route('/blur', methods=['POST'])
def clickbait():
    if not request.json:
        abort(400)

    subject_table = ['math', 'cs', 'chem', 'drawing', 'econ', 'music', 'cb']
    
    TruthTable = request.json['table']
    video_id = request.json['video_id']

    res = get_video_data(video_id)
    title = res['title']
    category = res['categoryId']

    # instant return based on category
    if category != MUSIC and category not in CLASSIFY_SET: 
        resp = jsonify({'result': 0})

    else:
        # if music category
        if category == MUSIC and TruthTable['music'] == 1: 
            resp = jsonify({'result': 1})
        elif category == MUSIC and TruthTable['music'] != 1: 
            resp = jsonify({'result': 0})
        else:
            is_cb = process_and_predict_clickbait_data(title)
            if bool(is_cb): 
                resp = jsonify({'result': 0})
            else:
                guess_subject = process_and_predict_classify_data(title)
                if TruthTable[[subject_table[guess_subject]] == 1: resp = jsonify({'result': 1})
                else: resp = jsonify({'result': 0})


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





if __name__ == '__main__':
    app.run(debug=False, threaded=False)
