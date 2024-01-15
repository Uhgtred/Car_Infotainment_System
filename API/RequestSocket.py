#!/usr/bin/env python3
# @author: Markus Kösters

from flask_restful import Resource

from BusTransactions import BusInterfaceFactory


class RequestSocket(Resource):
    """
    Class to create a direct socket-connection to the server.
    """

    def get(self) -> list | None:
        """
        Method to create a direct socket-connection to the server.
        :return: List containing the ip and port that the connection will run on if connection is successful. Else returns None.
        """
        socket = BusInterfaceFactory.produceUDP_Transceiver()
        # returning socket-address and port if socket does exist (from open socket)
        if socket is not None:
            return list(socket.bus.sock.getsockname())
        return None
