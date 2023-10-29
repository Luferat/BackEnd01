# API REST JSON usando uma coleção de dicionários.
 
from flask import Flask, jsonify, request

app = Flask(__name__)

things = [
    {
        "id": 1,
        "name": "Bagulho",
        "description": "Apenas um bagulho",
        "location": "Em uma caixa"
    },
    {
        "id": 2,
        "name": "Tranqueira",
        "description": "Apena uma tranqueira qualquer",
        "location": "Em um gaveteiro qualquer"
    },
    {
        "id": 3,
        "name": "Bagulete",
        "description": "Apenas um bagulete qualquer",
        "location": "Em um caixote na esquina"
    }
]


@app.route('/things', methods=['GET'])
def get_all():
    return jsonify(things)


@app.route('/things/<int:id>', methods=['GET'])
def get_one(id):
    for thing in things:
        if thing.get('id') == id:
            return jsonify(thing)


@app.route('/things', methods=['POST'])
def new():
    new_thing = request.get_json()
    things.append(new_thing)
    return jsonify(things)


@app.route('/things/<int:id>', methods=['PUT', 'PATCH'])
def edit(id):
    edited_thing = request.get_json()
    for index, thing in enumerate(things):
        if thing.get('id') == id:
            things[index].update(edited_thing)
            return jsonify(things[index])


@app.route('/things/<int:id>', methods=['DELETE'])
def delete(id):
    for index, thing in enumerate(things):
        if thing.get('id') == id:
            del (things[index])
            return jsonify(things)


app.run(port=3000, host='localhost', debug=True)
