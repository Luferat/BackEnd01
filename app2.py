# API REST JSON usando um arquivo de persistência.

from flask import Flask, jsonify, request
import json

app = Flask(__name__)


def db_open():
    with open('things.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def db_save(data):
    with open('things.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


@app.route('/things', methods=['GET'])
def get_all():
    things = db_open()
    return jsonify(things)


@app.route('/things/<int:id>', methods=['GET'])
def get_one(id):
    things = db_open()
    for thing in things:
        if thing.get('id') == id:
            return jsonify(thing)


@app.route('/things', methods=['POST'])
def new():
    things = db_open()
    new_thing = request.get_json()
    things.append(new_thing)
    db_save(things)
    return jsonify(things)


@app.route('/things/<int:id>', methods=['PUT', 'PATCH'])
def edit(id):
    things = db_open()
    edited_thing = request.get_json()
    for index, thing in enumerate(things):
        if thing.get('id') == id:
            things[index].update(edited_thing)
            db_save(things)
            return jsonify(things[index])


@app.route('/things/<int:id>', methods=['DELETE'])
def delete(id):
    things = db_open()
    for index, thing in enumerate(things):
        if thing.get('id') == id:
            del (things[index])
            db_save(things)
            return jsonify(things)


app.run(port=3000, host='localhost', debug=True)
