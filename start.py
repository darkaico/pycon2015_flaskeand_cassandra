import json

from flask import (
    Flask,
    render_template,
    request,
)

from pycon_cassandra import manager

app = Flask(__name__)


@app.route('/create/keyspace', methods=['POST'])
def create_keyspace_action():
    keyspace = request.form['keyspace']

    manager.create_keyspace_from_name(keyspace)

    return json.dumps({'message': 'ok'})


@app.route('/create/model', methods=['POST'])
def create_model_action():
    keyspace = request.form['keyspace']

    manager.create_model(keyspace)

    return json.dumps({'message': 'Model created'})


@app.route('/beer', methods=['POST'])
def drink_beer_action():
    keyspace = request.form['keyspace']
    brand = request.form['brand']

    result = manager.fill_model(keyspace, brand)

    return json.dumps(result)


@app.route("/")
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True)
