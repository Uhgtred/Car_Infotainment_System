#!/usr/bin/env python3
# @author: Markus Kösters

import socket

from BusTransactions import Bus
from . import SocketConfigs


class UdpSocket(Bus):

    def __init__(self, config: SocketConfigs.UdpSocketConfig):
        sockLibrary = config.busLibrary
        self._setupSocket(sockLibrary)
        self.__IP = config.IPAddress
        self.__PORT = config.port

    def readBus(self) -> bytes:
        pass

    def writeBus(self, message: bytes) -> None:
        """
        Method for writing message to UDP socket.
        :param message: Message that will be sent to UDP-socket.
        """
        self.__sock.sendto(message, (self.__IP, self.__PORT))

    def _setupSocket(self, sock) -> None:
        self.__sock = sock(socket.AF_INET, socket.SOCK_DGRAM)
