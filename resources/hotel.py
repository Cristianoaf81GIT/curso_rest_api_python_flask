# -*- coding:utf-8 -*-
from flask_restful import Resource, reqparse

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
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome',)
    argumentos.add_argument('estrelas', type=float)
    argumentos.add_argument('diaria', type=float)
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id=hotel_id)
        if hotel:
            return hotel

        return {'message': 'Hotel not found.'}, 404  # status code

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {'hotel_id': hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        novo_hotel = {'hotel_id': hotel_id, **dados}

        hotel = Hotel.find_hotel(hotel_id=hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return hotel, 200

        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'hotel: ' + hotel_id + ' was deleted.'}