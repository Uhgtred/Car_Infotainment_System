#!/usr/bin/env python3
# @author Markus Kösters

from .BusEncodings import ArduinoSerialEncoding


class EncodingInterface:
    """
    Container to make all Encodings available through one object.
    """

    @staticmethod
    def arduinoSerialEncoding():
        return ArduinoSerialEncoding()
