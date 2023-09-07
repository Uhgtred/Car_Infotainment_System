#!/usr/bin/env python3
# @author      Markus Kösters

from abc import abstractmethod, ABC


class Message(ABC):

    @abstractmethod
    def encodeMessage(self, message: str) -> any:
        """
        Method used for encoding messages to send by bus.
        :param message: Message that shall be sent to bus and therefore has to be encoded.
        :return: Encoded message in the specified format.
        """
        ...

    @abstractmethod
    def decodeMessage(self, message: any) -> str:
        """
        Method used for decoding messages received from bus.
        :param message: message that has been received from bus.
        :return: Decoded message in string format.
        """
        ...


class SerialMessage(Message):
    """
    Class for reading and writing a Serial-connection.
    """
    __messageEndByte = b'&'
    __ID_endByte = b'#'  # Symbol signing the end of a CAN-ID transmission.

    def encodeMessage(self, message: str) -> bytes:
        """
        Method used for encoding messages to send by bus.
        :param message: Message that shall be sent to bus and therefore has to be encoded.
        :return: Encoded message in the specified format.
        """
        message = message.encode() + self.__messageEndByte
        return message

    def decodeMessage(self, message: bytes) -> str:
        """
        Method used for decoding messages received from bus.
        :param message: message that has been received from bus.
        :return: Decoded message in string format.
        """
        decodedMessageEndByte = self.__messageEndByte.decode()
        message = message.decode()
        if message.endswith(decodedMessageEndByte):
            message = message.removesuffix(decodedMessageEndByte)
        return message

    @property
    def endByte(self) -> bytes:
        """
        Getter-Method for the End-byte of a Serial-message.
        :return: end-byte as bytes.
        """
        return self.__messageEndByte

    @property
    def ID_endByte(self) -> bytes:
        """
        Getter-Method for the symbol that signs the end of a CAN-ID transmission.
        :return: ID_endByte as bytes.
        """
        return self.__ID_endByte
