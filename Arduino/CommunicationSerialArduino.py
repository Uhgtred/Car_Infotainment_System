#!/usr/bin/env python3
# @author      Markus Kösters
import logging
import time

from Arduino import InterfaceSerialArduino


class CommunicationSerialArduino(InterfaceSerialArduino):

    def __int__(self):
        super().__init__()
        self.__lineBlocked = False

    async def sendSerialMessage(self, message: bytes) -> None:
        """
        Sending a message to the microcontroller
        :param message: message that shall be sent
        """
        await self.__waitForOpenSerialPort()
        message += b'&'
        logging.info(f'sending: {message} length: {len(message)} to: {self.connection}')  # needs to go into a logging-module
        self.connection.flushOutput()
        self.connection.write(message)
        logging.debug(f'Pausing module SendSerialToArduino.sendSerialMessage for {self.connection.delay}s')
        # time.sleep(self.connection.delay)  # probably not needed anymore with async

    async def readSerialMessage(self, notification: classmethod) -> None:
        """
        A loop reading messages from microcontroller and returning them to a defined method as an argument
        :param notification: method that the received message shall be passed to
        """
        while True:
            await self.__waitForOpenSerialPort()
            self.__lineBlocked = True
            message = await self.connection.readline()
            notification(message.decode())
            self.__lineBlocked = False

    async def __serialPortLock(self):
        """
        Setting a lock for the serial-port
        :return: <bool> lock-status
        """
        return self.__lineBlocked

    async def __waitForOpenSerialPort(self):
        """
        Waiting for the lock to release
        :return: None
        """
        while self.__lineBlocked:
            await self.__serialPortLock()
        return
