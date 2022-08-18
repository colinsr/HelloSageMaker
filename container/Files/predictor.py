from __future__ import print_function
import os
import flask

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')

app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return flask.Response(response='\n', status=200, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():
    return flask.Response(response="Hello SageMaker!\n", status=200, mimetype='text/csv')