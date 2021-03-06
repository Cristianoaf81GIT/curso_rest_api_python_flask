# -*- coding:utf-8 -*-
from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
        # select * from hotel
        return {'hoteis': [hotel.json() for hotel in  HotelModel.query.all()]}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()

    argumentos.add_argument('nome', 
            required=True, type=str, help='The field "name" cannot be left blank')

    argumentos.add_argument('estrelas', required=True,
                            type=float, help='Cannot convert to float.',)

    argumentos.add_argument('diaria', type=float,
                            required=True, help='Cant convert to float.')

    argumentos.add_argument('cidade', 
            required=True, type=str, help="the field 'cidade' cannot left blank")

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id=hotel_id)
        if hotel:
            return hotel.json()

        return {'message': 'Hotel not found.'}, 404  # status code

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': "Hotel id '{}' already exists.".format(hotel_id)}, 400
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message':'An internal error ocurred trying to save hotel.'}, 500

        return hotel.json(), 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id=hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id,**dados)
        try:
            hotel.save_hotel()
        except:
            return {'message':'An internal error ocurred trying to update hotel.'}, 500
        return hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()            
            except:
                return {'message': 'An internal server error ocurred trying to delete hotel.'}, 500
            return {'message': 'hotel: ' + hotel_id + ' was deleted.'}
        return {'message': 'hotel not found'}, 404


