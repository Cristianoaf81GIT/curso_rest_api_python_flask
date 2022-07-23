# -*- coding:utf-8 -*-
from flask_restful import Resource, reqparse
from models.usuario import UserModel 


class User(Resource):
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


