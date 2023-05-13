from util.conexion import *
from marshmallow import Schema, fields, ValidationError

def must_not_be_blank(data):
    if not data:
        raise ValidationError("Campo vacio.")


class ContactUs(Schema):

    nombre_solicitante = fields.String(required=True, validate=must_not_be_blank)
    email = fields.Email(required=True, validate=must_not_be_blank)
    telefono = fields.String(required=True, validate=must_not_be_blank)
    asunto = fields.String(required=True, validate=must_not_be_blank)
    mensaje = fields.String(required=True, validate=must_not_be_blank)

class ContactUsQuery:

    def __init__(self):
        self.conexion_ = conexion()

    def insert_(self, data):

        cursor = self.conexion_.conector.cursor()

        insql = "INSERT INTO contact_us (nombre_solicitante, email, telefono, asunto, mensaje) VALUES (%s, %s, %s, %s, %s)"
        datos = (data['nombre_solicitante'], data['email'], data['telefono'], data['asunto'], data['mensaje'])
        cursor.execute(insql, datos)
        self.conexion_.conector.commit()