#!/usr/bin/env python3
# @author Markus Kösters

from .BusEncodings import ArduinoSerialEncoding


class EncodingContainer:
    """
    Container to make all Encodings available through one object.
    """

    @staticmethod
    def arduinoSerialEncoding():
        return ArduinoSerialEncoding()
