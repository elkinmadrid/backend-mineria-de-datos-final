from flask import Blueprint, jsonify, request
from util.jwt import token_required
from api.dataset.dataset import QueryDataSet
import numpy as np

import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


algorithm = Blueprint('algorithm', __name__)


@algorithm.route('/api/v1/algorithm', methods=['POST'])
@token_required
def get_all(self):
    le = preprocessing.LabelEncoder()
    query_ = QueryDataSet()
    data = query_.get_all()

    original_df = pd.DataFrame(data)
    original_df.drop('id', axis=1, inplace=True)

    le = preprocessing.LabelEncoder()

    le.fit(original_df.loc[:, 'companyname'])
    original_df['companyname'] = le.transform(
        original_df.loc[:, 'companyname'])

    le.fit(original_df.loc[:, 'fueltype'])
    original_df['fueltype'] = le.transform(original_df.loc[:, 'fueltype'])

    le.fit(original_df.loc[:, 'doornumber'])
    original_df['doornumber'] = le.transform(original_df.loc[:, 'doornumber'])

    le.fit(original_df.loc[:, 'carbody'])
    original_df['carbody'] = le.transform(original_df.loc[:, 'carbody'])

    le.fit(original_df.loc[:, 'drivewheel'])
    original_df['drivewheel'] = le.transform(original_df.loc[:, 'drivewheel'])

    le.fit(original_df.loc[:, 'enginelocation'])
    original_df['enginelocation'] = le.transform(
        original_df.loc[:, 'enginelocation'])

    le.fit(original_df.loc[:, 'enginetype'])
    original_df['enginetype'] = le.transform(original_df.loc[:, 'enginetype'])

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


    data = {
        "mae": mae,
        "mse": mse,
        "score": r2
    }

    return jsonify(data=data, status=200)
