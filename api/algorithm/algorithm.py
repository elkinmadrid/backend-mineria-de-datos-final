from api.dataset.dataset import QueryDataSet

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class Algorithm ():

    def predict(self, data, X_train, y_train, X_test, y_test):

        reg = linear_model.LinearRegression()
        reg = reg.fit(X_train, y_train)

        """#TEST PREDICCIÓN
        predecir valores de una variable dependiente (Y) a partir de una variable independiente (X) utilizando un modelo de regresión. 
        """
        Y_pred = reg.predict(X_test)
        print(Y_pred)

        """#**SCORE**"""

        print(reg.score(X_test, y_test))

        # Calcular el MAE
        mae = mean_absolute_error(y_test, Y_pred)
        # Calcular el MSE
        mse = mean_squared_error(y_test, Y_pred)
        # Calcular el R-cuadrado
        r2 = r2_score(y_test, Y_pred)
        data['companyname'] = self.data_homologada[data['companyname']]
        data['enginetype'] = self.data_homologada[data['enginetype']]
        data['fueltype'] = self.data_homologada[data['fueltype']]
        data['doornumber'] = self.data_homologada[data['doornumber']]
        data['carbody'] = self.data_homologada[data['carbody']]
        data['enginelocation'] = self.data_homologada[data['enginelocation']]
        data['drivewheel'] = self.data_homologada[data['drivewheel']]


        dataframe = pd.DataFrame({
            'fueltype': [data['fueltype']],
            'doornumber': [data['doornumber']],
            'carbody': [data['carbody']],
            'drivewheel': [data['drivewheel']],
            'enginelocation': [data['enginelocation']],
            'carlength': [data['carlength']],
            'carwidth': [data['carwidth']],
            'carheight': [data['carheight']],
            'enginetype': [data['enginetype']],
            'enginesize': [data['enginesize']],
            'horsepower': [data['horsepower']],
            'companyname': [data['companyname']]
        })
        # Realizar la predicción en los valores ingresados manualmente
        prediccion = reg.predict(dataframe)
        print('El precio predecido es: ', prediccion)


        response = {
            "mae": mae,
            "mse": mse,
            "score": r2,
            "price": prediccion[0]
        }
        return response

    data_homologada = {}

    def homologacion(self, n, n2):

        for valor_a, valor_b in zip(n, n2):
            self.data_homologada[valor_a] = valor_b

    def entrenamiento_predecir(self, data_predecir):
        le = preprocessing.LabelEncoder()
        query_ = QueryDataSet()
        data = query_.get_all()

        original_df = pd.DataFrame(data)
        original_df.drop('id', axis=1, inplace=True)

        le = preprocessing.LabelEncoder()

        le.fit(original_df.loc[:, 'companyname'])
        original_df['companyname'] = le.transform(
            original_df.loc[:, 'companyname'])

        n = list(le.classes_)
        n2 = le.transform(n)
        self.homologacion(n, n2)

        le.fit(original_df.loc[:, 'fueltype'])
        original_df['fueltype'] = le.transform(original_df.loc[:, 'fueltype'])

        n = list(le.classes_)
        n2 = le.transform(n)
        self.homologacion(n, n2)

        le.fit(original_df.loc[:, 'doornumber'])
        original_df['doornumber'] = le.transform(
            original_df.loc[:, 'doornumber'])

        n = list(le.classes_)
        n2 = le.transform(n)
        self.homologacion(n, n2)

        le.fit(original_df.loc[:, 'carbody'])
        original_df['carbody'] = le.transform(original_df.loc[:, 'carbody'])

        n = list(le.classes_)
        n2 = le.transform(n)
        self.homologacion(n, n2)

        le.fit(original_df.loc[:, 'drivewheel'])
        original_df['drivewheel'] = le.transform(
            original_df.loc[:, 'drivewheel'])

        n = list(le.classes_)
        n2 = le.transform(n)
        self.homologacion(n, n2)

        le.fit(original_df.loc[:, 'enginelocation'])
        original_df['enginelocation'] = le.transform(
            original_df.loc[:, 'enginelocation'])

        n = list(le.classes_)
        n2 = le.transform(n)
        self.homologacion(n, n2)

        le.fit(original_df.loc[:, 'enginetype'])
        original_df['enginetype'] = le.transform(
            original_df.loc[:, 'enginetype'])

        n = list(le.classes_)
        n2 = le.transform(n)
        self.homologacion(n, n2)

        """#ENTRENAMIENTO DEL MODELO
        Esta operación se utiliza para dividir un conjunto de datos en dos conjuntos diferentes: uno para entrenamiento del modelo y otro para evaluación del modelo. 
        En este caso, se ha establecido en 0.3, lo que significa que el 30% de los datos se utilizarán para la evaluación del modelo, y el 70% se utilizarán para entrenar el modelo.
        **Datos de entrenamiento:**
        X_train, y_train   (características y valores objetivo)

        **Datos de prueba:**
        X_test, y_test     (características y valores objetivo)
        """

        X_train, X_test, y_train, y_test = train_test_split(
            original_df.drop('price', axis=1), original_df.price, test_size=0.3)

        """#Regresión lineal"""

        result = self.predict(data_predecir, X_train, y_train, X_test, y_test)
        return result
