#!/usr/bin/env python3
# @author: Markus Kösters

import socket

from BusTransactions import Bus
from . import SocketConfigs


class UdpSocket(Bus):

    def __init__(self, config: SocketConfigs.UdpSocketConfig):
        sockLibrary = config.busLibrary
        self._setupSocket(sockLibrary)
        self.__address = (config.IPAddress, config.port)

    def readBus(self) -> bytes:
        """
        Method that reads the UDP socket.
        :return: Message read from the UDP socket.
        """
        return self.__sock.recvfrom(1024)

    def writeBus(self, message: bytes) -> None:
        """
        Method for writing message to UDP socket.
        :param message: Message that will be sent to UDP-socket.
        """
        self.__sock.sendto(message, self.__address)

    def _setupSocket(self, sock: socket.socket) -> None:
        """
        Private Method for setting up UDP-socket.
        :param sock: socket that will be setup and bound.
        """
        self.__sock = sock(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind(self.__address)
