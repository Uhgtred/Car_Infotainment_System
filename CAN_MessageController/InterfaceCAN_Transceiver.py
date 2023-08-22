#!/usr/bin/env python3
# @author      Markus Kösters

import abc
from abc import abstractmethod

import can
from Arduino import CommunicationSerialArduino


class InterfaceCAN_Transceiver(abc):

    @abstractmethod
    def receiveCan_Message(self,  receiver: CommunicationSerialArduino.readSerialMessage) -> can.Message:
        """
        Interface for receiving a CAN-Message
        :return: CAN-Message
        """
        ...

    @abstractmethod
    def sendCAN_Message(self, transmitter: CommunicationSerialArduino.sendSerialMessage, message: bytes) -> None:
        """
        Interface for sending messages to the CAN-Bus
        :param transmitter: microcontroller which will be sending the messages to the CAN-Bus
        :param message: message that shall be sent
        """
        ...
