from flask import Flask
from flask_cors import CORS
from api.dataset.route import dataset
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

from api.users.route import usuarios
from api.contact_us.contact_us_route import contact_us
from api.algorithm.route import algorithm
app.register_blueprint(usuarios)
app.register_blueprint(dataset)
app.register_blueprint(contact_us)
app.register_blueprint(algorithm)


JWT_SECRETKEY = os.environ['JWT_SECRETKEY']
app.config['SECRET_KEY']=JWT_SECRETKEY

if __name__ == "__main__":
    app.run(debug=True)
