#!/usr/bin/env python3
# @author      Markus Kösters

import atexit
import time
from abc import abstractmethod, ABC
import serial

from .Message import Message, SerialMessage


class Bus(ABC):
    """
    Class for prescribing the structure of how to build a bus-connection.
    """

    @abstractmethod
    def read(self) -> any:
        """
        Method for reading a single message from a Bus.
        """
        ...

    @abstractmethod
    def send(self, message: Message.encodeMessage) -> None:
        """
        Method for properly closing a connection to a Microcontroller.
        :param message: Message that shall be sent to the bus
        """
        ...


class ArduinoSerialBus(Bus):
    """
    Class for async Serial-communication with arduino
    """
    __sendBuffer: list = []
    __busConnection: serial.Serial

    def __init__(self, busConnection: serial.Serial):
        # Close serial connection, when program closes
        atexit.register(self.exitHandler)
        self.__busConnection = busConnection.open()
        self.messageFormatter = SerialMessage()

    def read(self) -> bytes:
        """
        Read a single Serial-Message from the bus.
        """
        # prioritising writing to the bus
        while len(self.__sendBuffer) > 0:
            time.sleep(0.1)
        message = self.__executeBlocking(self.__busConnection.readline)
        return message
        #callbackMethod(self.name, message)
        """
        This code-block might be more stable then the one-liner
        """
        # message = b''
        # receivedByte = b''
        # endByte = b'&'
        # while receivedByte != endByte:
        #    message += self.connection.read()

    def send(self, message: str | bytes) -> None:
        """
        Sending a message to the microcontroller.
        :param message:
        :return:
        """
        message = self.messageFormatter.encodeMessage(message)
        self.__busConnection.write(message)

    @staticmethod
    def __executeBlocking(method: callable, args: list[bytes] = None) -> bytes | None:
        """
        TODO: check if this is still needed!
        Executing a blocking read-/write operation on serial-bus
        :param method: method that shall be executed
        :param args: (necessary for write-operation) list of messages <bytes> that shall be sent
        :return: bytes if read-operation is being executed
        """
        if args:
            method(args.pop(0))
        else:
            answer = method()
            return answer

    def exitHandler(self) -> None:
        """
        Closing the Serial-connection, when class-destructor is being called
        """
        self.__busConnection.close()
