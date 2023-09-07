#!/usr/bin/env python3
# @author      Markus Kösters
from abc import ABC, abstractmethod

import serial


class Microcontroller(ABC):

    @abstractmethod
    def open(self) -> object:
        """
        Method for opening a connection to a microcontroller.
        :return: Object of the Microcontroller that has been connected
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Method for closing a connection to a microcontroller.
        """
        ...

    @property
    @abstractmethod
    def port(self) -> str:
        """
        Getter-method for the port-variable
        :return: port
        """
        ...


class Arduino(Microcontroller):
    """
    Class for handling a serial-connection to an Arduino.
    """
    __device: serial.Serial | None = None
    __baudRate: int = 115200
    __port: str = '/dev/ttyACM0'

    def __init__(self, port: str = __port, baudRate: int = __baudRate):
        self.__port: str = port
        self.__baudRate: int = baudRate

    def close(self) -> None:
        """
        Method for closing a Serial-connection to Microcontrollers.
        """
        if self.__device.is_open:
            self.__device.close()
        self.__device = None

    def open(self) -> serial.Serial:
        """
        Method for opening a Serial-connection to Microcontrollers.
        :return: Object of thee arduino-connection, that can be used to communicate with.
        """
        if not self.__device:
            self.__initArduino()
            self.__device.open()
        return self.__device

    def __initArduino(self):
        """
        Initializing the microcontrollers serial-bus-settings.
        """
        self.__device = serial.Serial()
        self.__device.baud = self.__baudRate
        self.__device.port = self.__port

    @property
    def port(self) -> str:
        """
        Getter-method for the serial-port
        :return: port <str>
        """
        return self.__port
