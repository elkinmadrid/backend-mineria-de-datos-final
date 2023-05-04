from flask import Blueprint, request, jsonify, current_app
import uuid
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .users import QueryUsers


usuarios = Blueprint('usuarios', __name__)


@usuarios.route('/register', methods=['POST'])
def signup_user():

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')
    data['public_id'] = str(uuid.uuid4())
    data['password'] = hashed_password
    query_ = QueryUsers()
    query_.insert_(data)

    return jsonify({'message': 'registered successfully'})


@usuarios.route('/login', methods=['POST'])
def login_user():

    auth = request.get_json()

    if not auth or not auth['username'] or not auth['password']:
        return jsonify('could not verify', 401)

    query_ = QueryUsers()
    user = query_.get_user_by_username(auth['username'])

    if check_password_hash(user[3], auth['password']):
        token = jwt.encode({'public_id': user[1], 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return jsonify('could not verify',  401)
