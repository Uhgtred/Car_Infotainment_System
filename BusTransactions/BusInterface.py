#!/usr/bin/env python3
# @author: Markus Kösters

from typing import Protocol

from BusTransactions.Encoding import Encoding


class Bus(Protocol):
    """
    Protocol for prescribing the structure of a bus-instance.
    """

    def readBus(self) -> any:
        """
        Method for reading from a bus.
        """
        pass

    def writeBus(self, message: any) -> None:
        """
        Method for writing to a bus.
        :param message: Message that shall be sent to the bus.
        """
        pass


class BusInterface:
    """
    Class for communication with a variety of bus-systems.
    """

    def __init__(self, bus: Bus, encoding: Encoding):
        """
        :param bus: Bus that shall be communicated with. Needs to follow the protocol Bus.
        :param encoding: Encoding that will be used to make the messages compliant to the bus.
        """
        self.__stopFlag: bool = False
        self.encoding = encoding
        self.bus = bus

    def readSingleMessage(self) -> Encoding:
        """
        Read and decode a single message from the bus.
        :return: Decoded message.
        """
        message = self.bus.readBus()
        return self.encoding.decode(message)

    def readBusUntilStopFlag(self, callbackMethod: callable, stopFlag: bool = False) -> None:
        """
        Reading messages from a bus in a loop until stopFlag is raised.
        :param callbackMethod: Method that the received messages shall be sent to.
                                Needs to accept one argument which is the message read from the bus.
        :param stopFlag: When true reading-loop stops.
        :TODO: check if this can be done asynchronously
        """
        if not stopFlag:
            message = self.bus.readBus()
            callbackMethod(self.encoding.decode(message))
            self.readBusUntilStopFlag(callbackMethod, self.stopFlag)

    def writeSingleMessage(self, message: any) -> None:
        """
        Sending an encoded message to the bus.
        :param message: Message that will be sent to the bus.
        """
        encodedMessage = self.encoding.encode(message)
        self.bus.writeBus(encodedMessage)

    @property
    def stopFlag(self) -> bool:
        """
        Getter-Method for the stop-flag.
        :return: Stop-flag.
        """
        return self.__stopFlag

    @stopFlag.setter
    def stopFlag(self, state: bool) -> None:
        """
        Setter-method for the stop-flag.
        :param state: Stop-flag state that will be set.
        """
        self.__stopFlag = state
