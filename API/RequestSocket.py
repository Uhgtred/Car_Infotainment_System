#!/usr/bin/env python3
# @author: Markus Kösters

from flask_restful import Resource

from BusTransactions import BusInterfaceFactory


class RequestSocket(Resource):
    """
    Class to create a direct socket-connection to the server.
    """

    def get(self) -> int:
        """
        Method to create a direct socket-connection to the server.
        :return: The port that the connection will run on if connection is successful. Else returns None.
        """
        socket = BusInterfaceFactory.produceUDP_Transceiver()
        # returning socket-port if socket does exist (from open socket)
        return socket.bus.sock.getsockname()[1]
