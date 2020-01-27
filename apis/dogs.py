from flask_restplus import Namespace, Resource, fields
from flask import Flask, jsonify

api = Namespace('Dog', description='Dogs related operations')

DOGS = [
  {'id': 'guenu', 'name': 'Gueralt'},
  {'id': 'guenu', 'name': 'Gueralt'},
  {'id': 'guenu', 'name': 'Gueralt'},
]

@api.route('/')
class DogList(Resource):
  def get(self):
    return jsonify({ "list": DOGS })

@api.route('/<id>')
@api.param('id', 'The dog identifier')
class Dog(Resource):
  def get(self, id):
    return jsonify({ "dados": DOGS[0] })

# conxao com o banco
# from dbConnection import Db
# db = Db()
# users = list(db.find('usuarios'))
# return db.count('usuarios')
