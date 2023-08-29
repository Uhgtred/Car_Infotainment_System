#!/usr/bin/env python3
# @author      Markus Kösters

from abc import ABC, abstractmethod

from Arduino import ArduinoConnector


class InterfaceSerialArduino(ABC):

    @abstractmethod
    async def sendSerialMessage(self, message: bytes) -> None:
        """
        Interface for sending Message to microcontroller through serial connection
        :param message: message that shall be sent to the microcontroller
        """
        ...

    @abstractmethod
    async def readSerialMessage(self, callbackMethod: callable) -> None:
        """
        Interface for reading a single message from Arduino
        :param callbackMethod: method, that shall be called when a message has been received
                                and which the message is being passed to as an argument
        :return: message in bytes-format to the callbackMethod. Decode by using message.decode()
        """
        ...

    @abstractmethod
    def subscribeSerialReadLoop(self, callbackMethod: callable) -> None:
        """
        Interface for subscribing to a Loop reading all messages passed from arduino
        :param callbackMethod: method, that shall be called when a message has been received
                                and which the message is being passed to as an argument
        :return: message in bytes-format to the callbackMethod. Decode by using message.decode()
        """
        ...
