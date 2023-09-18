import os
from flask import Flask, Response
from modelos.modelos import db
from vistas.vistas import VistasLogIn, VistaSignIn, VistaUsuario
from flask_restful import Api
from flask_jwt_extended import JWTManager

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///test.db")
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['JWT_SECRET_KEY'] = 'secret_key'
application.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

api = Api(application)
api.add_resource(VistaSignIn, '/users')
api.add_resource(VistasLogIn, '/users/auth')
api.add_resource(VistaUsuario, '/users/me')

jwt = JWTManager(application)

@jwt.unauthorized_loader
def missing_token(callback):
    return Response(status=400)

@jwt.expired_token_loader
def missing_token(jwt_header, jwt_payload):
    return Response(status=401)

@jwt.invalid_token_loader
def invalid_token(callback):
    return Response(status=401)

@application.route("/users/ping")
def index():
    return "pong-pong",200

if __name__ == "__main__":
    application.run(host = "0.0.0.0", port = 5000, debug = True)
    