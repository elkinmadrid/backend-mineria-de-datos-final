from flask import Blueprint, jsonify
from util.jwt import token_required
from .dataset import QueryDataSet

dataset = Blueprint('dataset', __name__)


@dataset.route('/api/v1/dataset', methods=['GET'])
@token_required
def get_all(self):
    query_ = QueryDataSet()
    data = query_.get_all()

    return jsonify(data=data, status=200)


