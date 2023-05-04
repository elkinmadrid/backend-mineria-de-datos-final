from marshmallow import Schema, fields
from util.conexion import *


class Users(Schema):

    public_id = fields.String(required=True)
    name = fields.String(required=True)
    password = fields.String(required=True)


class QueryUsers():

    def __init__(self):
        self.conexion_ = conexion()

    def insert_(self, data):

        cursor = self.conexion_.conector.cursor()

        insql = "INSERT INTO users (public_id, name, password) VALUES (%s, %s, %s)"
        datos = (data['public_id'], data['name'], data['password'])
        cursor.execute(insql, datos)
        self.conexion_.conector.commit()

    def get_user_by_username(self, username):

        query = 'SELECT * FROM users WHERE name = %s'

        cursor = self.conexion_.conector.cursor()
        datos = (username,)
        cursor.execute(query, datos)
        return cursor.fetchone()
