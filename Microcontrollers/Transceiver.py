#!/usr/bin/env python3
# @author      Markus Kösters
import atexit
from abc import ABC, abstractmethod

import serial

from Events import Event
from .Microcontroller import Arduino
from .Message import Message, SerialMessage
from .Bus import ArduinoSerialBus


class Transceiver(ABC):

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
    def sendMessage(self, message: Message.encodeMessage) -> None:
        """
        Method that sends messages to a bus. There needs to be a concrete
        implementation of the abstract Transceiver-class for each bus.
        :param message: message that shall be sent to the bus
        """
        ...


class CAN_Transceiver(Transceiver):
    """
    Method for sending and receiving can-messages through serial connection to arduino.
    """
    arduino: serial.Serial = Arduino()
    name: str = 'can_transceiver'
    exit_: bool = False

    def __init__(self):
        atexit.register(self.exitHandler)
        self.messageFormatter = SerialMessage()
        self.__bus = ArduinoSerialBus(self.arduino)
        self.__messageFormatter = SerialMessage()

    def receiveMessage(self, callbackMethod: Event.sendMessage, loop: bool = True) -> None:
        """
        Method for transmitting and receiving CAN-Messages from arduino-serial-bus.
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
        Executing the read-operation in the serial-bus class and sending data to eventmanager
        :param callbackMethod: Method that the message <str> shall be passed to.
        """
        message = self.__bus.read()
        message = self.messageFormatter.decodeMessage(message)
        callbackMethod(self.name, message)

    def sendMessage(self, message: SerialMessage.encodeMessage) -> None:
        """
        Method that send messages to serial-bus of Arduino
        :param message: <str> CAN-Message that shall be sent.
        """
        self.__bus.send(self.__messageFormatter.encodeMessage(message))

    def exitHandler(self):
        """
        Method for handling ordinary program exit.
        """
        self.exit_ = True
        self.arduino.close()
