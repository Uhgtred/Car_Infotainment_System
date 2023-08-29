#!/usr/bin/env python3
# @author      Markus Kösters

import asyncio
import logging
import threading

import Arduino
from Arduino import ArduinoConnector, InterfaceSerialArduino


class CommunicationSerialArduino:
    """
    Class for async Serial-communication with arduino
    """
    # connection object to the serial-bus
    connection = ArduinoConnector().arduino
    __sendBuffer = []

    async def sendSerialMessage(self, message: InterfaceSerialArduino.sendSerialMessage) -> None:
        """
        Sending a message to the microcontroller.
        Use like this: asyncio.run(sendSerialMessage(b"Hello World"))
        :param message: message that shall be sent
        """
        # Appending end-byte
        message = self.__applyProtocol(message)
        logging.info(f'sending: {message} length: {len(message)} to: {self.connection}')  # needs to go into a logging-module
        # self.connection.flushOutput()
        self.__sendBuffer.append(message)
        await self.__executeBlocking(self.connection.write, self.__sendBuffer)

    @staticmethod
    def __applyProtocol(message: InterfaceSerialArduino.sendSerialMessage) -> bytes:
        """
        Applying message protocol to message that is about to be sent
        :param message: message that the protocol needs to be applied on
        :return: message with applied protocol
        """
        # attaching message end-byte to the message
        message += b'&'
        return message

    def subscribeSerialReadLoop(self, callbackMethod: InterfaceSerialArduino.readSerialMessage) -> None:
        """
        This is meant for the notification of subscribers of an event-manager.
        Pass a notifier-method with argument <bytes> message.
        Example: subscribeSerialReadLoop(notifier) --> def notifier(self, message: bytes): ...
        :param callbackMethod: call-back function for passing the message to
        """
        thread = threading.Thread(target=lambda: asyncio.run(self.__readLoop(callbackMethod)))
        thread.start()
        # asyncio.run(self.readSerialMessage(callbackMethod))

    async def __readLoop(self, callbackMethod: InterfaceSerialArduino.readSerialMessage) -> None:
        """
        Reading serial-messages in an async-loop
        :param callbackMethod: method that the received message shall be passed to
        """
        async with self.readSerialMessage(callbackMethod):
            await asyncio.Future()

    async def readSerialMessage(self, callbackMethod: InterfaceSerialArduino.readSerialMessage) -> None:
        """
        A loop reading messages from microcontroller and returning them to a defined method as an argument
        Use this with asyncio.run() or await or just use the method: subscribeSerialReadLoop,
        which will handle that stuff for you.
        :param callbackMethod: method that the received message shall be passed to
        """
        # prioritising writing to the bus
        if len(self.__sendBuffer) > 0:
            return
        message = await self.__executeBlocking(self.connection.readline)
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
    async def __executeBlocking(method: connection, args: list[bytes] = None) -> bytes | None:
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

    def __del__(self):
        """
        Closing the Serial-connection, when class-destructor is being called
        """
        Arduino.ArduinoConnector().close()
