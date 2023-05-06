from util.conexion import *

class QueryDataSet():

    def __init__(self):
        self.conexion_ = conexion()

    def delete_row(self, id):
        query = 'DELETE FROM dataset WHERE id = %s'

        datos = (id,)

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query, datos)
        self.conexion_.conector.commit()

    def get_all(self):
        
        query = 'SELECT * FROM dataset ORDER BY ID DESC'

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        data = []
        for result in results:

            data.append({
                "id": result[0],
                "edad": result[1],
                "created_at": result[2],
                "anemia": result[3],
                "creatinina_fosfoquinasa": result[4],
                "diabetes": result[5],
                "fraccion_de_eyeccion": result[6],
                "presion_arterial_alta": result[7],
                "plaquetas": result[8],
                "creatinina_serica": result[9],
                "sodio_serico": result[10],
                "sexo": result[11],
                "fumador": result[12],
                "Seguimiento_dias": result[13],
                "Muerte": result[14]

            })
        return data