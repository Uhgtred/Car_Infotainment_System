#!/usr/bin/env python3
# @author: Markus Kösters

from .SerialBusModule import SerialBus, SerialBusConfig


class BusFactory:
    """
    Class for producing Bus-instances.
    """

    @staticmethod
    def produceSerialBusArduino() -> SerialBus:
        """
        Method for creating an instance of a SerialBus.
        :return: SerialBus-instance.
        """
        config = SerialBusConfig('/dev/ttyACM0', 115200)
        return SerialBus(config)
