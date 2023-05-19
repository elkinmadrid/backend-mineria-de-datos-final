from flask import Blueprint, jsonify, request
from util.jwt import token_required
from .algorithm import Algorithm

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


algorithm = Blueprint('algorithm', __name__)


@algorithm.route('/api/v1/algorithm', methods=['POST'])
@token_required
def get_all(self):

    try:
        body = request.json

        predecir = Algorithm()
        data = predecir.entrenamiento_predecir(body)

        return jsonify(data=data, status=200)

    except Exception as inst:
        print(inst)
        return {'message': 'Error inesperado'}, 500
