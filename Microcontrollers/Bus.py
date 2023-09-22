#!/usr/bin/env python3
# @author      Markus Kösters

from abc import ABC, abstractmethod
from typing import NamedTuple
import serial


class BusConfig(NamedTuple):
    bus: any
    port: str
    baudRate: int


class Bus(ABC):

    __config: BusConfig

    def __init__(self, config: BusConfig):
        self.__config = config

    @abstractmethod
    def open(self) -> __config.bus:
        """
        Method for opening a connection to a bus.
        :return: Object of the bus that has been connected
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Interface-method for closing a connection to a bus.
        """


class SerialBusArduino(Bus):
    """
    Class for handling a serial-connection to an Arduino.
    """

    __config: BusConfig

    def __init__(self, config: BusConfig):
        super().__init__(config)
        self.__config.bus = None

    def open(self) -> __config.bus:
        """
        Method for opening a Serial-connection to Microcontrollers.
        :return: Object of thee arduino-connection, that can be used to communicate with.
        """
        try:
            if not self.__config.bus:
                self.__initArduino()
        except Exception as e:
            raise Exception(f'Could not start Arduino-connection: {e}')
        return self.__config.bus

    def close(self) -> None:
        """
        Method for closing a connection to a bus.
        """
        self.__config.bus.close()

    def __initArduino(self):
        """
        Initializing the microcontrollers serial-bus-settings.
        """
        self.__config.bus = serial.Serial()
        self.__config.bus.baudRate = self.__config.baudRate
        self.__config.bus.port = self.__config.port
        self.__config.bus.open()
