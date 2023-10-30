#!/usr/bin/env python3
# @author      Markus Kösters

import atexit
from abc import ABC, abstractmethod
import serial

from BusTransactions.Buses.SerialBusModule.SerialBusConfig import SerialBusConfig


class SerialBusInterface(ABC):

    @abstractmethod
    def readBus(self) -> bytes:
        """
        Interface-method for reading from a bus.
        :return: Bytes containing the message.
        """
        pass

    @abstractmethod
    def writeBus(self, message: bytes) -> None:
        """
        Interface-method for writing to a bus.
        :param message: Message that shall be sent to the bus.
        """
        pass


class SerialBus(SerialBusInterface):
    """
    Class for handling a serial-connection to an Arduino. And reading/writing messages to it.
    """

    def __init__(self, config: SerialBusConfig):
        # check if the busLibrary-object has already been instanced
        if callable(config.busLibrary):
            self.bus = config.busLibrary()
        else:
            self.bus = config.busLibrary
        self.__port = config.port
        self.__baudRate = config.baudRate
        self.bus: serial.Serial = self.__setupBus()
        # Making sure the bus is closed when instance dies.
        atexit.register(self.bus.close)

    def readBus(self) -> bytes:
        """
        Method for reading from the serial-bus.
        :return: Bytes containing the message.
        """
        return self.bus.read()

    def writeBus(self, message: bytes) -> None:
        """
        Method for writing to the serial-bus.
        :param message: Message that shall be sent to the bus.
        """
        self.bus.write(message)

    def __setupBus(self) -> serial.Serial:
        """
        Initializing the microcontroller bus-settings.
        """
        bus = self.bus
        bus.baudrate = self.__baudRate
        bus.port = self.__port
        if not bus.isOpen():
            bus.open()
        return bus
