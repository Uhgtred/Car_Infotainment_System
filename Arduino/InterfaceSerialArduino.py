#!/usr/bin/env python3
# @author      Markus Kösters

from abc import ABC, abstractmethod

from Arduino import Arduino


class InterfaceSerialArduino(ABC):

    @abstractmethod
    async def sendSerialMessage(self, message: bytes) -> None:
        """
        Interface for sending Message to microcontroller through serial connection
        :param message: message that shall be sent to the microcontroller
        """
        ...

    @abstractmethod
    async def readSerialMessage(self, notification: classmethod) -> None:
        """
        Interface for reading a message from Arduino
        :return: message in bytes-format. Decode by using message.decode()
        """
        ...

    # def __exit__(self):
    #     """
    #     could potentially lead to closing the serial-connection before being able to use it
    #     :return:
    #     """
    #     print('!!!!SERIAL CONNECTION GOT CLOSED!!!!')
    #     self.connection.close()
