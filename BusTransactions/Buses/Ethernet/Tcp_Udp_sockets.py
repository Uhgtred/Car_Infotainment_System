#!/usr/bin/env python3
# @author: Markus Kösters

import socket

from BusTransactions.Bus import Bus
from . import SocketConfigs


class UdpSocket(Bus):

    def __init__(self, config: SocketConfigs.UdpSocketConfig):
        sockLibrary = config.busLibrary
        self.sock = None
        self.__messageSize = config.messageSize
        self.__address = (config.IPAddress, config.port)
        self._setupSocket(sockLibrary)

    def readBus(self) -> bytes:
        """
        Method that reads the UDP socket.
        :return: Message read from the UDP socket.
        """
        return self.sock.recvfrom(self.__messageSize)

    def writeBus(self, message: bytes) -> None:
        """
        Method for writing message to UDP socket.
        :param message: Message that will be sent to UDP-socket.
        """
        self.sock.sendto(message, self.__address)

    def _setupSocket(self, sock: socket) -> None:
        """
        Private Method for setting up UDP-socket.
        :param sock: socket that will be setup and bound.
        """
        self.sock = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
        self.sock.bind(self.__address)
