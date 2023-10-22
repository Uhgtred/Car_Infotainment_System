#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass

from .Buses import SerialBusConfig, SerialBus
from .BusTransceiver import Bus, BusTransceiver
from BusTransactions.Encoding import Encoding


class BusFactory:
    """
    Factory for creating an instance of a bus-transceiver.
    """

    @staticmethod
    def produceBusTransceiver(config: dataclass, encoding: Encoding, busModule: type(Bus)):
        """
        Method for producing an instance of a bus-transceiver.
        :param busModule: Bus-Class that will be communicated with
                        (NOT bus-library e.g. serial.Serial but e.g. BusTransactions.Buses.SerialBusModule.SerialBus).
        :param config: Configuration that sets the parameters of the bus.
        :param encoding: Encoding that decides the format of the messages.
        """
        busModule = busModule(config)
        # check if encoding has already been instanced
        if callable(encoding):
            encoding = encoding()
        transceiver = BusTransceiver(busModule, encoding)
        return transceiver

    @staticmethod
    def produceSerialTransceiver(config: SerialBusConfig, encoding: Encoding):
        """
        Method for creating an instance of a serial-bus transceiver.
        :param config: Configuration that sets the parameters of the bus.
        :param encoding: Encoding that decides the format of the messages.
        """
        busModule = SerialBus(config)
        # check if encoding has already been instanced
        if callable(encoding):
            encoding = encoding()
        return BusTransceiver(busModule, encoding)
