# API REST JSON usando um gerador de Ids para o POST.

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

db = 'things.json'


def db_open():
    try:
        with open(db, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except Exception as e:
        print(f"Erro ao abrir arquivo JSON: {e}")


def db_save(data):
    try:
        with open(db, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar arquivo JSON: {e}")


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
    all_ids = [reg['id'] for reg in things]
    next_id = max(all_ids) + 1
    new_thing = request.get_json()
    new_thing["id"] = next_id
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
