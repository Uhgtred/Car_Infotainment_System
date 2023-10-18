#!/usr/bin/env python3
# @author Markus Kösters
import time
from typing import Protocol


class Bus(Protocol):

    def readBus(self) -> bytes:
        """
        Interface-method for reading from a bus.
        :return: Bytes containing the message.
        """
        pass

    def writeBus(self, message: bytes) -> None:
        """
        Interface-method for writing to a bus.
        :param message: Message that shall be sent to the bus.
        """
        pass


class BusCommunicator:
    """
    General class to communicate with a bus.
    """

    __busses: list

    def __init__(self, bus: Bus):
        self.__busInstance = bus
        self.__busses.append(bus)

    @property
    def getReader(self) -> callable:
        """
        Getter-method to gain access to the reader-method of the bus-instance.
        :return: Reader-method for the bus-instance.
        """
        return self.__busInstance.readBus

    @property
    def getWriter(self) -> callable:
        """
        Getter-method to gain access to the writer-method of the bus-instance.
        :return: Writer-method for the bus-instance.
        """
        return self.__busInstance.writeBus
