from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tlqkftprtm@localhost/totothon'

from Server import mysql
mysql.db.create_all()

from Server.routes import index, image
app.register_blueprint(index.app, url_prefix='/')
app.register_blueprint(image.app, url_prefix='/image')
