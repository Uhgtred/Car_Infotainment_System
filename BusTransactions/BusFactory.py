#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass

from BusTransactions.BusTransceiver import Bus, Encoding, BusTransceiver


class BusFactory:
    """
    Factory for creating an instance of a bus-transceiver.
    """

    @staticmethod
    def produceBusTransceiver(bus: type(Bus), config: dataclass, encoding: Encoding):
        """
        Method for producing an instance of a bus-transceiver.
        :param bus: Bus that will be communicated with.
        :param config: Configuration that sets the parameters of the bus.
        :param encoding: Encoding that decides the format of the messages.
        """
        bus = bus(config)
        transceiver = BusTransceiver(bus, encoding)
        return transceiver
