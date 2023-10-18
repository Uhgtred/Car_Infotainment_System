#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass

from BusTransactions.BusTransceiver import Bus, Encoding, BusTransceiver


class BusFactory:

    @staticmethod
    def produceBusTransceiver(bus: type(Bus), config: dataclass, encoding: Encoding):
        bus = bus(config)
        transceiver = BusTransceiver(bus, encoding)
        return transceiver


