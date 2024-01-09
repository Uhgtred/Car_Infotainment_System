#!/usr/bin/env python3
# @author: Markus Kösters
from flask import Flask
from flask_restful import Resource, Api

from BusTransactions import BusInterfaceFactory

app = Flask('InfotainmentAPI')
api = Api(app)

class SocketRequest(Resource):

    def get(self, port: int):
        return BusInterfaceFactory.produceUDP_Transceiver(port)

api.add_resource(SocketRequest, '/getSocketObject')

if __name__ == '__main__':
    app.run(debug=True)