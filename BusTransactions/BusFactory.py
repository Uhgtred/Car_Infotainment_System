#!/usr/bin/env python3
# @author: Markus Kösters

from . import EncodingInterface, Buses
from .BusInterface import BusInterface
from BusTransactions.Encoding import Encoding


class BusFactory:
    """
    Factory for creating an instance of a bus-transceiver.
    """

    @staticmethod
    def produceBusTransceiver(bus: Buses.Factory, encoding: Encoding) -> BusInterface:
        """
        Method for producing an instance of a bus-transceiver.
        :param bus: Bus-Class that will be communicated with, produced by Factory-class in Buses-Module.
        :param encoding: Encoding that decides the format of the messages.
        """
        bus = bus()
        # check if encoding has already been instanced
        if callable(encoding):
            encoding = encoding()
        transceiver = BusInterface(bus, encoding)
        return transceiver

    @staticmethod
    def produceSerialTransceiver() -> BusInterface:
        """
        Method for creating an instance of a serial-bus transceiver that connects to arduino.
        """
        encoding = EncodingInterface.arduinoSerialEncoding
        busModule = Buses.Factory.produceSerialBusArduino()
        # check if encoding has already been instanced
        if callable(encoding):
            encoding = encoding()
        return BusInterface(busModule, encoding)
