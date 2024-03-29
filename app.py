# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import (
    User, 
    UserRegister, 
    UserLogin, 
    UserLogout, 
    UserConfirm
) 
from resources.site import Site, Sites 
from flask_jwt_extended import JWTManager
from os import environ
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['FLASK_DEBUG'] = environ.get('APP_DEBUG_MODE') == 'True'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader 
def verifica_blacklist(self,token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header,jwt_payload):
    return jsonify({'message': 'You have been logged out!'}), 401

@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Sites, '/sites')
api.add_resource(Site, '/sites/<string:url>')
api.add_resource(UserConfirm, '/confirmacao/<int:user_id>')

# aula 88 continua em 2:55

if __name__ == "__main__":
    from sql_alchemy import banco
    banco.init_app(app)  # run only in main
    from flask_bcrypt_util import bcrypt # run only in main
    bcrypt.init_app(app)
    app.run(debug=True, load_dotenv=True)
