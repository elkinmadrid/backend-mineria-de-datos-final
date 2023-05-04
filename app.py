from flask import Flask
from api.dataset.route import dataset
import os

app = Flask(__name__)

from api.users.route import usuarios
app.register_blueprint(usuarios)
app.register_blueprint(dataset)


JWT_SECRETKEY = os.environ['JWT_SECRETKEY']
app.config['SECRET_KEY']=JWT_SECRETKEY
app.run(debug=True)
