#!/usr/bin/env python3
# @author: Markus Kösters

from .Buses import BusFactory
from .Encoding import EncodingFactory
from .BusInterface import BusInterface


class BusInterfaceFactory:
    """
    Factory for creating an instance of a bus-transceiver.
    """

    @staticmethod
    def produceBusTransceiver(bus: type(BusFactory), encoding: type(EncodingFactory)) -> BusInterface:
        """
        Method for producing an instance of a bus-transceiver.
        :param bus: Bus-Class that will be communicated with, produced by Factory-class in Buses-Module.
        :param encoding: Encoding that decides the format of the messages.
        """
        # check if encoding has already been instanced
        if callable(encoding):
            encoding = encoding()
        transceiver = BusInterface(bus, encoding)
        return transceiver

    @classmethod
    def produceSerialTransceiver(cls) -> BusInterface:
        """
        Method for creating an instance of a serial-bus transceiver that connects to arduino.
        """
        encoding = EncodingFactory.arduinoSerialEncoding
        busModule = BusFactory.produceSerialBusArduino()
        return cls.produceBusTransceiver(busModule, encoding)

    @classmethod
    def produceUDP_Transceiver(cls) -> BusInterface:
        """
        Method for creating an instance of an udp-socket.
        :return:
        """
        encoding = EncodingFactory.socketEncoding()  # needs to get its own encoding
        busModule = BusFactory.produceUdpSocket()
        return cls.produceBusTransceiver(busModule, encoding)
