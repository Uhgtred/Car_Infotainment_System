#!/usr/bin/env python3
# @author: Markus Kösters
from flask import Flask, jsonify
from flask_restful import Resource, Api

from BusTransactions import BusInterfaceFactory

app = Flask('InfotainmentAPI')
api = Api(app)


class SocketRequest(Resource):
    """
    Class to create a direct socket-connection to the server.
    """

    def get(self, port: int) -> int:
        """
        Method to create a direct socket-connection to the server.
        :param port: port that the connection will run on.
        :return: The port that the connection will run on if connection is successful. Else returns None.
        """
        socket = BusInterfaceFactory.produceUDP_Transceiver(port)
        # returning socket-port if socket does exist (from open socket)
        return socket.bus.sock.getsockname()[1]


api.add_resource(SocketRequest, '/getSocketObject/<int:port>')

if __name__ == '__main__':
    app.run(debug=True)
