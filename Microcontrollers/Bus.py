#!/usr/bin/env python3
# @author      Markus Kösters
import asyncio
import atexit
from abc import abstractmethod, ABC

import serial

from .Message import Message, SerialMessage
from .Microcontroller import Arduino


class Bus(ABC):
    """
    Class for prescribing the structure of how to build a bus-connection.
    """

    @abstractmethod
    def read(self, callbackMethod: callable) -> None:
        """
        Method for reading a single message from a Bus.
        """
        ...

    @abstractmethod
    def readLoop(self, callbackMethod: callable) -> None:
        """
        Method for reading from a Bus in a loop.
        """
        ...

    @abstractmethod
    def send(self, message: Message.encodeMessage) -> None:
        """
        Method for properly closing a connection to a Microcontroller.
        """
        ...


class ArduinoSerialBus(Bus):
    """
    Class for async Serial-communication with arduino
    """
    __sendBuffer: list = []
    __busConnection: serial.Serial

    def __init__(self, busConnection: serial.Serial):
        # Close serial connection, if program closes
        atexit.register(self.exitHandler)
        self.__busConnection = busConnection
        self.messageFormatter = SerialMessage()

    def read(self, callbackMethod: callable) -> None:
        """
        Read a single Serial-Message from the bus.
        :param callbackMethod: Method that the received message shall be passed to.
        """
        asyncio.run(self.readSerialMessage(callbackMethod))

    def readLoop(self, callbackMethod: callable) -> None:
        """
        Reading serial-messages in an async-loop
        :param callbackMethod: Method that the received message shall be passed to.
        """
        while True:
            self.read(callbackMethod)

    def send(self, message: SerialMessage.encodeMessage) -> None:
        """
        Sending a message to the microcontroller.
        :param message:
        :return:
        """
        message = self.messageFormatter.encodeMessage(message)
        asyncio.run(self.sendSerialMessage(message))

    async def sendSerialMessage(self, message: bytes) -> None:
        """
        Sending a message to the microcontroller.
        Use like this: asyncio.run(sendSerialMessage(b"Hello World"))
        :param message: message that shall be sent
        """
        self.__sendBuffer.append(message)
        await self.__executeBlocking(self.__busConnection.write, self.__sendBuffer)

    async def readSerialMessage(self, callbackMethod: callable) -> None:
        """
        A loop reading messages from microcontroller and returning them to a defined method as an argument
        Use this with asyncio.run() or await or just use the method: subscribeSerialReadLoop,
        which will handle that stuff for you.
        :param callbackMethod: Method that the received message shall be passed to.
        """
        # prioritising writing to the bus
        if len(self.__sendBuffer) > 0:
            return
        message = await self.__executeBlocking(self.__busConnection.readline)
        message = self.messageFormatter.decodeMessage(message)  # turning byte-message to string
        await callbackMethod(message)

        """
        This code-block might be more stable then the one-liner
        """
        # message = b''
        # receivedByte = b''
        # endByte = b'&'
        # while receivedByte != endByte:
        #    message += self.connection.read()

    @staticmethod
    async def __executeBlocking(method: callable, args: list[bytes] = None) -> bytes | None:
        """
        Executing a blocking read-/write operation on serial-bus
        :param method: method that shall be executed
        :param args: (necessary for write-operation) list of messages <bytes> that shall be sent
        :return: bytes if read-operation is being executed
        """
        if args:
            await method(args.pop(0))
        else:
            answer = await method()
            return answer

    def exitHandler(self):
        """
        Closing the Serial-connection, when class-destructor is being called
        """
        self.__busConnection.close()
