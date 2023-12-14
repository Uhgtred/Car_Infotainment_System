#!/usr/bin/env python3
# @author Markus Kösters
from typing import Protocol

from .BusEncodings import ArduinoSerialEncoding


class EncodingProtocol(Protocol):
    """
    Protocol for prescribing the structure of the encoding.
    """

    @staticmethod
    def decode(message: any) -> any:
        """
        Method for decoding a message received from a bus.
        :param message: Message from bus that needs to be decoded.
        """
        pass

    @staticmethod
    def encode(message: any) -> any:
        """
        Method for encoding a message that will be sent to a bus.
        :param message: Message that needs to be encoded.
        """
        pass


class EncodingInterface:
    """
    Container to make all Encodings available through one object.
    """

    @staticmethod
    def arduinoSerialEncoding():
        return ArduinoSerialEncoding()
