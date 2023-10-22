#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass

from BusTransactions.BusTransceiver import Bus, BusTransceiver
from BusTransactions.Encoding import Encoding


class BusFactory:
    """
    Factory for creating an instance of a bus-transceiver.
    """

    @staticmethod
    def produceBusTransceiver(config: dataclass, encoding: Encoding, bus: type(Bus)):
        """
        Method for producing an instance of a bus-transceiver.
        :param bus: Bus-Class that will be communicated with
                    (NOT bus-library e.g. serial.Serial but e.g. BusTransactions.Busses.SerialBusModule.SerialBus).
        :param config: Configuration that sets the parameters of the bus.
        :param encoding: Encoding that decides the format of the messages.
        """
        bus = bus(config)
        transceiver = BusTransceiver(bus, encoding)
        return transceiver
