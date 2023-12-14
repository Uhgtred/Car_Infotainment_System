#!/usr/bin/env python3
# @author: Markus Kösters
from .Buses import BusFactory
from .Encoding import EncodingInterface, EncodingInterface
from .BusInterface import BusInterface


class BusInterfaceFactory:
    """
    Factory for creating an instance of a bus-transceiver.
    """

    @staticmethod
    def produceBusTransceiver(bus: BusFactory, encoding: EncodingInterface) -> BusInterface:
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
        busModule = BusInterfaceFactory.produceSerialBusArduino()
        # check if encoding has already been instanced
        if callable(encoding):
            encoding = encoding()
        return BusInterface(busModule, encoding)
