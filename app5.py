# API RESTful JSON.

from flask import Flask, jsonify, request, abort, make_response
import json

app = Flask(__name__)

db = 'things.json'


def db_open():
    try:
        with open(db, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except Exception as e:
        print(f"Erro ao abrir arquivo JSON: {e}")
        return False


def db_save(data):
    try:
        with open(db, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            return True
    except Exception as e:
        print(f"Erro ao salvar arquivo JSON: {e}")
        return False


def not_found():
    abort(make_response({'message': 'Não encontrado'}, 404))


@app.route('/things', methods=['GET'])
def get_all():
    things = db_open()
    if (len(things) > 0):
        return jsonify(things)
    not_found()


@app.route('/things/<int:id>', methods=['GET'])
def get_one(id):
    things = db_open()
    for index, thing in enumerate(things):
        if thing.get('id') == id:
            return jsonify(thing)
    not_found()


@app.route('/things', methods=['POST'])
def new():
    things = db_open()
    all_ids = [reg['id'] for reg in things]
    if all_ids:
        next_id = max(all_ids) + 1
    else:
        next_id = 1
    new_thing = request.get_json()
    new_thing["id"] = next_id
    things.append(new_thing)
    if db_save(things):
        return jsonify(new_thing), 201
    else:
        return jsonify({'status': 'error', 'message': 'Falha ao salvar dados'}), 500


@app.route('/things/<int:id>', methods=['PUT', 'PATCH'])
def edit(id):
    things = db_open()
    edited_thing = request.get_json()
    for index, thing in enumerate(things):
        if thing.get('id') == id:
            things[index].update(edited_thing)
            if db_save(things):
                return jsonify(things[index])
            else:
                return jsonify({'status': 'error', 'message': 'Falha ao salvar dados'}), 500
    not_found()


@app.route('/things/<int:id>', methods=['DELETE'])
def delete(id):
    things = db_open()
    for index, thing in enumerate(things):
        if thing.get('id') == id:
            del (things[index])
            if db_save(things):
                return jsonify({'status': 'success', 'message': 'Apagado com sucesso'})
            else:
                return jsonify({'status': 'error', 'message': 'Falha ao salvar dados'}), 500
    not_found()


app.run(port=3000, debug=True)
