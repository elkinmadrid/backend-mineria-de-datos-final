from util.conexion import *


class QueryDataSet():

    def __init__(self):
        self.conexion_ = conexion()

    def delete_row(self, id):
        query = 'DELETE FROM dataset_cars WHERE id = %s'

        datos = (id,)

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query, datos)
        self.conexion_.conector.commit()

    def update_row(self, data, id):
        query = """
        UPDATE public.dataset_cars
        SET fueltype=%s, doornumber=%s, carbody=%s, drivewheel=%s, enginelocation=%s, carlength=%s, carwidth=%s, 
        carheight=%s, enginetype=%s, enginesize=%s, horsepower=%s, price=%s, companyname=%s
        WHERE id=%s
        """

        datos = (data['fueltype'], data['doornumber'], data['carbody'], data['drivewheel'], data['enginelocation'],
                 float(data['carlength']), float(data['carwidth']), float(
                     data['carheight']), data['enginetype'], float(data['enginesize']),
                 float(data['horsepower']),  float(data['price']), data['companyname'], id)

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query, datos)
        self.conexion_.conector.commit()

    def insert_row(self, data, id):
        query = """
        INSERT INTO public.dataset_cars
        (fueltype, doornumber, carbody, drivewheel, enginelocation, carlength, carwidth, 
        carheight, enginetype, enginesize, horsepower, price, companyname)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        datos = (data['fueltype'], data['doornumber'], data['carbody'], data['drivewheel'], data['enginelocation'],
                 float(data['carlength']), float(data['carwidth']), float(
                     data['carheight']), data['enginetype'], float(data['enginesize']),
                 float(data['horsepower']),  float(data['price']), data['companyname'])

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query, datos)
        self.conexion_.conector.commit()

    def get_all(self):

        query = 'SELECT * FROM dataset_cars ORDER BY ID ASC'

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        data = []
        for result in results:

            data.append({
                "id": result[0],
                "fueltype": result[1],
                "doornumber": result[2],
                "carbody": result[3],
                "drivewheel": result[4],
                "enginelocation": result[5],
                "carlength": result[6],
                "carwidth": result[7],
                "carheight": result[8],
                "enginetype": result[9],
                "enginesize": result[10],
                "horsepower": result[11],
                "price": result[12],
                "companyname": result[14]

            })
        return data

    def get_all_variable_category(self):
        query = """
            SELECT
                (SELECT ARRAY_AGG(DISTINCT companyname) FROM dataset_cars) AS companyname,
                (SELECT ARRAY_AGG(DISTINCT doornumber) FROM dataset_cars) AS doornumber,
                (SELECT ARRAY_AGG(DISTINCT enginelocation) FROM dataset_cars) AS enginelocation,
                (SELECT ARRAY_AGG(DISTINCT drivewheel) FROM dataset_cars) AS drivewheel,
                (SELECT ARRAY_AGG(DISTINCT fueltype) FROM dataset_cars) AS fueltype,
                (SELECT ARRAY_AGG(DISTINCT carbody) FROM dataset_cars) AS carbody,
                (SELECT ARRAY_AGG(DISTINCT enginetype) FROM dataset_cars) AS enginetype;
                
                """
        cursor = self.conexion_.conector.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        data = {
            'companyname': results[0][0],
            'doornumber': results[0][1],
            'enginelocation': results[0][2],
            'drivewheel': results[0][3],
            'fueltype': results[0][4],
            'carbody': results[0][5],
            'enginetype': results[0][6]
        }
        return data

    def carbody_price(self):
        query = """
            select carbody, COUNT(*) as amount_vehicule, 
            ROUND(MIN(price)::numeric, 2) AS min_price,
            ROUND(MAX(price)::numeric, 2) as max_price,
            ROUND(avg(price)::numeric, 2) as avg_price
            from dataset_cars dc 
            group by carbody order by carbody;
        
        """

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        data = []
        for row in results:
            data.append({
                'carbody': row[0],
                'amount_vehicule': row[1],
                'min_price': row[2],
                'max_price': row[3],
                'avg_price': row[4]
            })
        return data

    def fueltype_companyname_avg_price(self):
        query = """
            select fueltype as Tipo_Combustible, 
            companyname as Marca,
            ROUND(avg(price)::numeric, 2) as Precio_Promedio
            from dataset_cars
            group by fueltype, marca
            order by fueltype, marca;
        
        """

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        data = []
        for row in results:
            data.append({
                'fueltype': row[0],
                'companyname': row[1],
                'avg_price': row[2]
            })
        return data

    def avg_horsepower_companyname(self):
        query = """
            select companyname as Marca,
            ROUND(AVG(horsepower)::numeric,2) as Promedio_Potencia,
            ROUND(MIN(price)::numeric, 2) AS precio_minimo,
            ROUND(MAX(price)::numeric, 2) as precio_Maximo
            from dataset_cars dc
            group by companyname
            order by companyname;
        """

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        data = []
        for row in results:
            data.append({
                'companyname': row[0],
                'avg_horsepower': row[1],
                'min_price': row[2],
                'max_price': row[3]
            })
        return data
