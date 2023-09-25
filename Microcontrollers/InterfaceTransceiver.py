#!/usr/bin/env python3
# @author      Markus Kösters
import atexit
from abc import ABC, abstractmethod
from typing import NamedTuple

from Events import Event
from .Bus import Bus
from .Message import Message
from .BusReaderWriter import BusReaderWriter


class TransceiverConfig(NamedTuple):
    bus: Bus
    busReaderWriter: BusReaderWriter
    eventName: str


class InterfaceTransceiver(ABC):

    def __init__(self, config: TransceiverConfig):
        self.config = config

    @abstractmethod
    def receiveMessage(self, callbackMethod: Event.sendMessage, loop: bool = True) -> None:
        """
        Method that receives messages from a bus (optionally only one message).
        There needs to be a concrete implementation of the abstract Transceiver-class for each bus.
        :param callbackMethod: Method that the read message shall be passed to.
        :param loop: True: reading messages constantly, False: reading only one message.
        """
        ...

    @abstractmethod
    def sendMessage(self, message: str) -> None:
        """
        Method that sends messages to a bus. There needs to be a concrete
        implementation of the abstract Transceiver-class for each bus.
        :param message: message that shall be sent to the bus
        """
        ...


class Transceiver(InterfaceTransceiver):
    """
    Method for sending and receiving can-messages through serial connection to arduino.
    """
    name: str = 'can_transceiver'
    exit_: bool = False

    def __init__(self, config: TransceiverConfig):
        super().__init__(config)
        atexit.register(self.exitHandler)

    def receiveMessage(self, callbackMethod: Event.sendMessage, loop: bool = True) -> None:
        """
        Method for transmitting and receiving Messages from bus.
        :param callbackMethod: Method that the message <str> shall be passed to.
        :param loop: Defines if all Messages (True) shall be read from Bus or just a single Message(False).
        """
        if loop:
            while not self.exit_:
                self.__readMessageFromBusAndSendToEventManager(callbackMethod)
        else:
            self.__readMessageFromBusAndSendToEventManager(callbackMethod)

    def __readMessageFromBusAndSendToEventManager(self, callbackMethod: Event.sendMessage) -> None:
        """
        Executing the read-operation in the bus-class and sending data to eventmanager
        :param callbackMethod: Method that the message <str> shall be passed to.
        """
        message = self.config.busReaderWriter.read()
        callbackMethod(self.config.eventName, message)

    def sendMessage(self, message: str) -> None:
        """
        Method that sends messages to a bus.
        :param message: <str> Message that shall be sent.
        """
        self.config.busReaderWriter.send(message)

    def exitHandler(self):
        """
        Method for handling ordinary program exit.
        """
        self.exit_ = True
        self.config.bus.close()
