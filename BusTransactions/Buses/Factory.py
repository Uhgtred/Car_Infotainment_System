#!/usr/bin/env python3
# @author: Markus Kösters

from .SerialBusModule.SerialBus import SerialBus
from .SerialBusModule.SerialBusConfig import SerialBusConfig


class Factory:

    @staticmethod
    def produceSerialBusArduino():
        bus = SerialBus(SerialBusConfig)
        return bus
