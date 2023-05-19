from flask import Blueprint, jsonify, request
from util.jwt import token_required
from .dataset import QueryDataSet

dataset = Blueprint('dataset', __name__)


@dataset.route('/api/v1/dataset', methods=['GET'])
@token_required
def get_all(self):
    query_ = QueryDataSet()
    data = query_.get_all()

    return jsonify(data=data, status=200)


@dataset.route('/api/v1/dataset/categories', methods=['GET'])
@token_required
def get_categories(self):
    query_ = QueryDataSet()
    data = query_.get_all_variable_category()

    return jsonify(data=data, status=200)


@dataset.route('/api/v1/dataset/<id>', methods=['DELETE'])
@token_required
def delete(self, id):
    try:
        if not id:
            return jsonify(message="No ids provided.", status=400)
        query_ = QueryDataSet()
        query_.delete_row(id)

        return {'message': 'Registro eliminado'}, 200

    except Exception as inst:
        print(inst)
        return {'message': 'Error inesperado'}, 500


@dataset.route('/api/v1/dataset/<id>', methods=['PUT'])
@token_required
def update(self, id):
    try:
        if not id:
            return jsonify(message="No ids provided.", status=400)
        data = request.json
        query_ = QueryDataSet()
        query_.update_row(data, id)
        print(data)

        return {'message': 'Registro actualizado'}, 200

    except Exception as inst:
        print(inst)
        return {'message': 'Error inesperado'}, 500

@dataset.route('/api/v1/dataset', methods=['POST'])
@token_required
def insert(self):
    try:
       
        data = request.json
        query_ = QueryDataSet()
        query_.insert_row(data, id)
        print(data)

        return {'message': 'Registro insertado!'}, 201

    except Exception as inst:
        print(inst)
        return {'message': 'Error inesperado'}, 500