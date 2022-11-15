# -*- encoding: utf-8 -*-
from sql_alchemy import banco
from flask_bcrypt_util import bcrypt
from flask import request, url_for 
import requests
import os 

MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN_NAME')
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM_EMAIL = os.environ.get('TITLE')
FROM_TITLE = os.environ.get('FROM')

class UserModel(banco.Model):
    __tablename__ = 'usuarios'

    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40), nullable=True, unique=True)
    senha = banco.Column(banco.String(200), nullable=False) # garante tamanho para senha encriptada
    email = banco.Column(banco.String(200), nullable=True, unique=True)
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
        return requests.post(
                'https://api.mailgun.net/v3/{}/messages'
                .format(MAILGUN_DOMAIN),
                auth=('api', MAILGUN_API_KEY),
                data={
                    'from': '{} <{}>'.format(FROM_TITLE, FROM_EMAIL),
                    'to': self.email,
                    'subject': 'Confirmação de cadastro!',
                    'text': 'Confirme seu cadastro clicando no link a seguir: {}'.format(link),
                    'html': """
                        <html>
                            <p>Confirm seu cadastro clicando no link a seguir:
                            <a href="{}">Confirmar E-mail</a></p>
                        </html>
                    """.format(link)
                }
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

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None
