#!/usr/bin/env python3
# @author      Markus Kösters
import atexit
from abc import ABC, abstractmethod

from .Microcontroller import Arduino
from .Message import Message, SerialMessage
from .Bus import ArduinoSerialBus


class Transceiver(ABC):

    @abstractmethod
    def receiveMessage(self, callbackMethod: callable, loop: bool = True) -> None:
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
    arduino = Arduino()

    def __init__(self):
        atexit.register(self.exitHandler)
        self.__bus = ArduinoSerialBus(self.arduino.open())
        self.__messageFormatter = SerialMessage()

    def receiveMessage(self, callbackMethod: callable, loop: bool = True) -> None:
        """
        Method for transmitting and receiving CAN-Messages from arduino-serial-bus.
        :param callbackMethod: Method that the message <str> shall be passed to.
        :param loop: Defines if all Messages (True) shall be read from Bus or just a single Message(False).
        """
        if loop:
            self.__bus.readLoop(callbackMethod)
        else:
            self.__bus.read(callbackMethod)

    def sendMessage(self, message: SerialMessage.encodeMessage) -> None:
        """
        Method that send messages to serial-bus of Arduino
        :param message: <str> CAN-Message that shall be sent.
        """
        self.__bus.send(self.__messageFormatter.encodeMessage(message))

    def exitHandler(self):
        self.arduino.close()
