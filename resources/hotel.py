# -*- coding:utf-8 -*-
from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended  import jwt_required


# path /hoteis?cidade=nome_cidade&estrelas_min=num_estrelas&estrelas_max=num_estrelas&limit=num_de_registros&offset=controle_listagem
class Hoteis(Resource):
    path_params = reqparse.RequestParser()
    path_params.add_argument('cidade', type=str, default="", location="args")
    path_params.add_argument('estrelas_min', type=float, default=0, location="args")
    path_params.add_argument('estrelas_max', type=float, default=0, location="args")
    path_params.add_argument('diaria_min', type=float, default=0, location="args")
    path_params.add_argument('diaria_max', type=float, default=0, location="args")
    path_params.add_argument('limit', type=float, default=0, location="args")
    path_params.add_argument('offset', type=float, default=0, location="args")

    def get(self):        
        filters = Hoteis.path_params.parse_args()
 
        query = HotelModel.query
 
        if filters["cidade"]:
            query = query.filter(HotelModel.cidade == filters["cidade"])
        if filters["estrelas_min"]:
            query = query.filter(HotelModel.estrelas >= filters["estrelas_min"])
        if filters["estrelas_max"]:
            query = query.filter(HotelModel.estrelas <= filters["estrelas_max"])
        if filters["diaria_min"]:
            query = query.filter(HotelModel.diaria >= filters["diaria_min"])
        if filters["diaria_max"]:
            query = query.filter(HotelModel.diaria <= filters["diaria_max"])
        if filters["limit"]:
            query = query.limit(filters["limit"])
        if filters["offset"]:
            query = query.offset(filters["offset"])
 
        return {"hoteis": [hotel.json() for hotel in query]}


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

    argumentos.add_argument('site_id', 
                            required=True, type=int, help="field 'site_id' is required!")

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id=hotel_id)
        if hotel:
            return hotel.json()

        return {'message': 'Hotel not found.'}, 404  # status code
    
    @jwt_required()
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
    
    @jwt_required() 
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

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()            
            except:
                return {'message': 'An internal server error ocurred trying to delete hotel.'}, 500
            return {'message': 'hotel: ' + hotel_id + ' was deleted.'}
        return {'message': 'hotel not found'}, 404


