from flask import Blueprint
from util.jwt import token_required

dataset = Blueprint('dataset', __name__)


@dataset.route('/dataset', methods=['GET'])
@token_required
def get_all(self):
    return {
        "message": "Bienvenido!"

    }, 200
