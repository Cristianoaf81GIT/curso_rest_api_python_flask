# -*- coding:utf-8 -*-
from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_bcrypt_util import bcrypt 
from flask_jwt_extended import create_access_token

atributos = reqparse.RequestParser()
atributos.add_argument('login',
        type=str, required=True, help='the field cannot be left blank')
atributos.add_argument('senha',
        type=str, required=True, help='the field cannot be left blank')


class User(Resource):
    # /usuario/userId
    def get(self, user_id):
        user = UserModel.find_user(user_id=user_id)
        if user:
            return user.json()

        return {'message': 'User not found.'}, 404  # status code

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()            
            except:
                return {'message': 'An internal server error ocurred trying to delete hotel.'}, 500
            return {'message': 'user was successfully deleted.'}
        return {'message': 'user not found'}, 404


class UserRegister(Resource):
    # /cadasto
    def post(self):       
        dados = atributos.parse_args()
        if UserModel.find_by_login(dados['login']):
            return {'message': 
                    'The login "{}" already exists'.format(dados['login'])}, 400 
        user = UserModel(**dados)
        user.save_user()
        return {'message': 'User created successfully'}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])            
        is_password_valid = bcrypt.check_password_hash(str(user.senha),str(dados['senha']))
        # safe_str_cmp, from werkzeug.security import safe_str_cmp 
        if user and is_password_valid:
            token_de_acessso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acessso}, 200
        return {'message': 'The username or password is incorrect'}, 401


