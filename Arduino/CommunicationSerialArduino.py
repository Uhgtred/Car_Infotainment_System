#!/usr/bin/env python3
# @author      Markus Kösters
import asyncio
import logging

from .Arduino import Arduino
from .InterfaceSerialArduino import InterfaceSerialArduino


class CommunicationSerialArduino(InterfaceSerialArduino):
    """
    Class for Serial-communication with arduino
    """

    # lock for avoiding multiple concurrent access on serial bus
    __lineBlocked = False
    # connection object to the serial-bus
    connection = Arduino().arduino

    async def sendSerialMessage(self, message: bytes) -> None:
        """
        Sending a message to the microcontroller.
        Use like this: asyncio.run(sendSerialMessage(b"Hello World")
        :param message: message that shall be sent
        """
        await self.__waitForOpenSerialPort()
        # Appending end-byte
        message = self.__applyProtocol(message)
        logging.info(f'sending: {message} length: {len(message)} to: {self.connection}')  # needs to go into a logging-module
        self.connection.flushOutput()
        self.connection.write(message)

    @staticmethod
    def __applyProtocol(message: bytes) -> bytes:
        """
        Applying message protocol to message that is about to be sent
        :param message: message that the protocol needs to be applied on
        :return: message with applied protocol
        """
        message += b'&'
        return message

    def linkSerialReadLoopToNotification(self, notification: any) -> None:
        """
        This is meant for the notification of subscribers of an event-manager.
        Pass a notifier-method with argument <bytes> message.
        Example: linkSerialReadLoopToNotification(notifier) --> def notifier(self, message: bytes): ...
        :param notification: call-back function for passing the message to
        """
        asyncio.run(self.readSerialMessage(notification))

    async def readSerialMessage(self, notification: any) -> None:
        """
        A loop reading messages from microcontroller and returning them to a defined method as an argument
        Use this with asyncio.run() or await or just use the method: linkSerialReadLoopToNotification,
        which will handle that stuff for you.
        :param notification: method that the received message shall be passed to
        """
        while True:
            # prioritising writing to the bus
            if self.connection.out_waiting > 0:
                continue
            await self.__waitForOpenSerialPort()
            self.__lineBlocked = True
            """
            This block might be more stable then the one-liner
            """
            # message = b''
            # receivedByte = b''
            # endByte = b'&'
            # while receivedByte != endByte:
            #    message += self.connection.read()
            message = await self.connection.readline()
            notification(message.decode())
            self.__lineBlocked = False

    async def __serialPortLock(self) -> bool:
        """
        Setting a lock for the serial-port
        :return: <bool> lock-status
        """
        return self.__lineBlocked

    async def __waitForOpenSerialPort(self) -> None:
        """
        Waiting for the lock to release
        :return: None
        """
        while self.__lineBlocked:
            await self.__serialPortLock()
        return
