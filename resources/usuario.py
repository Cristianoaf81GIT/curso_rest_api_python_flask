# -*- coding:utf-8 -*-
from flask import make_response, render_template 
import traceback
from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_bcrypt_util import bcrypt 
from flask_jwt_extended import create_access_token, jwt_required, get_jti, get_jwt 
from blacklist import BLACKLIST


"""
" anotations:
" @jwt_required()
" @jwt.token_in_block_loader
" get_jwt
" verificar_blacklist(self, token)
"""

atributos = reqparse.RequestParser()

atributos.add_argument(
        'login',
        type=str, 
        required=True, 
        help='the field cannot be left blank'
)

atributos.add_argument(
        'senha',
        type=str, 
        required=True, 
        help='the field cannot be left blank'
)

atributos.add_argument('email', type=str)
atributos.add_argument('ativado', type=bool)


class User(Resource):
    # /usuario/userId
    def get(self, user_id):
        user = UserModel.find_user(user_id=user_id)
        if user:
            return user.json()

        return {'message': 'User not found.'}, 404  # status code
    
    @jwt_required()
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
        
        if (
            not dados.get('email') or 
            dados.get('email') is None
        ):
            return {
                'message': "The field 'email' cannot be left blank!"
            }, 400
        
        if UserModel.find_by_email(dados['email']):
            return  {
                'messsage': "the email '{}' already exists".format(dados['email'])
            }, 400

        if UserModel.find_by_login(dados['login']):
            return {
                'message': 
                    'The login "{}" already exists'.format(dados['login'])
            }, 400 
        
        user = UserModel(**dados)
        user.ativado = False
        
        try:
            user.save_user()
            user.send_confirmation_email()
        except:
            user.delete_user()
            traceback.print_exc()
            return {
                'message': 'An internal server error has been ocurred!'
            }, 500

        return {'message': 'User created successfully'}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])
        is_password_valid = bcrypt.check_password_hash(
                user.senha,
                str(dados['senha'])
        )
                               
        # safe_str_cmp, from werkzeug.security import safe_str_cmp 
        if user and is_password_valid:
            if user.ativado:
                token_de_acessso = create_access_token(identity=user.user_id)
                return {'access_token': token_de_acessso}, 200
            return {'message': 'User not confirmed!'}, 400
        return {'message': 'The username or password is incorrect'}, 401


class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] #jwt token indentifier
        if len(jwt_id) > 0:
            BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfuly!'}, 200


class UserConfirm(Resource):
    # /confirmacao/{user_id}
    @classmethod 
    def get(cls,user_id):
        user = UserModel.find_user(user_id)

        if not user:
            return {
                'message': "user id '{}' not found.".format(user_id)
            }, 404
        
        user.ativado = True
        user.save_user()
        #return {
        #    'message': 'user id "{}" confirmed successfully.'.format(user_id)
        #}, 200
        headers = {'Content-Type': 'text/html'}
        return make_response(
                render_template(
                    'user_confirm.html', 
                    email=user.email, 
                    usuario=user.login
                ),
                200,
                headers 
        )


