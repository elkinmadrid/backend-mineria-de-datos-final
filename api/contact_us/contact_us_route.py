from flask import Blueprint, jsonify, request
from util.jwt import token_required
from .contactUs import ContactUsQuery, ContactUs

contact_us = Blueprint('contact-us', __name__)


@contact_us.route('/api/v1/contact-us', methods=['POST'])
def add_contact_us():

    body_request = request.json
    validation = ContactUs().validate(body_request)
    if validation:
            return {'message': 'Validation errors', 'errors': validation}, 400
    query_ = ContactUsQuery()
    query_.insert_(body_request)

    return jsonify(message='Informacion creada', status_code=201), 201


@contact_us.route('/api/v1/contact-us', methods=['GET'])
@token_required
def get_info_contact_us(self):
     query_ = ContactUsQuery()
     data = query_.get_all_info()

     return jsonify(status_code=200, data=data), 200