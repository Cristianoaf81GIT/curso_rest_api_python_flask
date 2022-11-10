# -*- encoding: utf-8 -*-
from sql_alchemy import banco
from flask_bcrypt_util import bcrypt
from flask import request, url_for 

class UserModel(banco.Model):
    __tablename__ = 'usuarios'

    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40), nullable=True, unique=True)
    senha = banco.Column(banco.String(200), nullable=False) # garante tamanho para senha encriptada
    email = banco.Column(banco.string(200), nullable=True, unique=True)
    ativado = banco.Column(banco.Boolean, default=False)

    def __init__(self, login, senha, email, ativado):
        self.login = login
        self.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        self.email = email
        self.ativado = ativado       

    
    def send_confirmation_email(self):
        link = (
                request.url_root[:-1] + 
                url_for('userconfirm', user_id=self.user_id)
        )

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
            'email': self.email,
            'ativado': self.ativado
        }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
