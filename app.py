# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
# from sql_alchemy import banco

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
# banco.init_app(app)

@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


if __name__ == "__main__":
    from sql_alchemy import banco
    banco.init_app(app)  # run only in main
    app.run(debug=True)
