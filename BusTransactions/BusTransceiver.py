#!/usr/bin/env python3
# @author: Markus Kösters

from typing import Protocol


class Bus(Protocol):

    def readBus(self) -> any:
        pass

    def writeBus(self, message: any):
        pass


class Encoding(Protocol):

    def decode(self, message: any) -> any:
        pass

    def encode(self, message: any) -> any:
        pass


class BusTransceiver:
    # Flag for stopping bus-read.
    # !!! This will stop reading for all instances !!!
    # TODO: think of some better solution
    __stopFlag: bool

    def __init__(self, bus: Bus, encoding: Encoding):
        self.encoding = encoding
        self.bus = bus

    def readSingleMessage(self) -> Encoding.decode:
        message = self.bus.readBus()
        return self.encoding.decode(message)

    def readBusInLoop(self, callbackMethod: callable, stopFlag: bool = False) -> None:
        self.stopFlag = stopFlag
        while not self.stopFlag:
            message = self.bus.readBus()
            callbackMethod(self.encoding.decode(message))

    def sendSingleMessage(self, message: any) -> None:
        encodedMessage = self.encoding.encode(message)
        self.bus.writeBus(encodedMessage)

    @property
    def stopFlag(self) -> bool:
        return self.__stopFlag

    @stopFlag.setter
    def stopFlag(self, state: bool) -> None:
        self.__stopFlag = state
