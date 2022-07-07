# -*- coding:utf-8 -*-
from flask_restful import Resource

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'alpha hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de janeiro'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'hotel bravo',
        'estrelas': 4.4,
        'diaria': 380.34,
        'cidade': 'Santa Catarina'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'hotel charlie',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'São Tomé das Letras'
    },
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found.'}, 404  # status code

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
