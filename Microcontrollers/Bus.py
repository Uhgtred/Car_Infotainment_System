#!/usr/bin/env python3
# @author      Markus Kösters

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import NamedTuple
import serial


@dataclass
class BusConfig:
    """
    Bus-configuration-tuple
    :param bus: a callable class-object of the bus that shall be opened e.g.: serial.Serial.
    :param port: Port to which the bus is listening e.g.: '/dev/ttyACM0'
    :param baudRate: Baud-rate/frequency of the bus e.g.: 115200
    """
    bus: any
    port: str
    baudRate: int


class Bus(ABC):
    config: BusConfig

    def __init__(self, config: BusConfig):
        self.config = config

    @abstractmethod
    def open(self) -> any:
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

    config: BusConfig

    def __init__(self, config: BusConfig):
        super().__init__(config)

    def open(self) -> any:
        """
        Method for opening a Serial-connection to Microcontrollers.
        :return: Object of thee arduino-connection, that can be used to communicate with.
        """
        try:
            self.config.bus = self.__setupBus()
        except Exception as e:
            raise Exception(f'Could not start Arduino-connection: {e}')
        return self.config.bus

    def close(self) -> None:
        """
        Method for closing a connection to a bus.
        """
        self.config.bus.close()

    def __setupBus(self) -> object:
        """
        Initializing the microcontrollers bus-settings.
        """
        bus = serial.Serial()
        bus.baudRate = self.config.baudRate
        bus.port = self.config.port
        if not bus.isOpen():
            bus.open()
        return bus
