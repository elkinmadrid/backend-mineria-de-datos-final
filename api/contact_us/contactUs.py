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
        datos = (data['nombre_solicitante'], data['email'],
                 data['telefono'], data['asunto'], data['mensaje'])
        cursor.execute(insql, datos)
        self.conexion_.conector.commit()

    def get_all_info(self):

        cursor = self.conexion_.conector.cursor()

        sql = "SELECT * FROM contact_us"
        cursor.execute(sql)

        results = cursor.fetchall()
        dataMap = []
        data =  map(self.to_json, results)

        for item in data:
            dataMap.append(item)
        
        return dataMap

    def to_json(self, item):
            return {
            'nombre_solicitante': item[1],
            'email': item[2],
            'telefono': item[3],
            'asunto': item[4],
            'mensaje': item[5]
        }