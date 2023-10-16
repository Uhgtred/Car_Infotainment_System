#!/usr/bin/env python3
# @author      Markus Kösters
import atexit
from abc import ABC, abstractmethod
import serial


class Bus(ABC):

    @abstractmethod
    def open(self) -> any:
        """
        Method for opening a connection to a bus.
        :return: Object of the bus that has been connected
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Interface-method for closing a connection to a bus.
        """
        pass

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


class SerialBusArduino(Bus):
    """
    Class for handling a serial-connection to an Arduino. And reading/writing messages to it.
    """

    __bus: serial.Serial

    def __init__(self, port: str = '/dev/ttyACM0', baudRate: int = 115200):
        self.__port = port
        self.__baudRate = baudRate
        # making sure bus is closing when instance dies.
        atexit.register(self.close)

    def open(self) -> serial.Serial():
        """
        Method for opening a Serial-connection to a Microcontroller.
        :return: Object of the arduino-connection, that can be used to communicate with.
        """
        try:
            self.__bus = self.__setupBus()
        except Exception as e:
            raise Exception(f'Could not start Arduino-connection: {e}')
        return self.__bus

    def close(self) -> None:
        """
        Method for closing a connection to a bus.
        """
        self.__bus.close()

    def __setupBus(self) -> object:
        """
        Initializing the microcontrollers bus-settings.
        """
        bus = serial.Serial()
        bus.baudrate = self.__baudRate
        bus.port = self.__port
        if not bus.isOpen():
            bus.open()
        return bus

    def readBus(self) -> bytes:
        """
        Method for reading from the serial-bus.
        :return: Bytes containing the message.
        """
        return self.__bus.read()

    def writeBus(self, message: bytes) -> None:
        """
        Method for writing to the serial-bus.
        :param message: Message that shall be sent to the bus.
        """
        self.__bus.write(message)

