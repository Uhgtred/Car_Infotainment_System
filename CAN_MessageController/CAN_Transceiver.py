#!/usr/bin/env python3
# @author      Markus Kösters

import can

from Arduino import CommunicationSerialArduino
from .InterfaceCAN_Transceiver import InterfaceCAN_Transceiver


class CAN_Transceiver(InterfaceCAN_Transceiver):
    """
    Class for receiving and transmitting CAN-messages
    """

    def receiveCan_Message(self, receiver: CommunicationSerialArduino.readSerialMessage) -> can.Message:
        """
        Receiving CAN-message from Arduino
        :param receiver: method of class CommunicationSerialArduino, that is responsible for reading data from Arduino Serial port
        :return: can message of format can.Message
        """
        message = receiver()
        return message

    def __decryptCAN_Message(self, message: bytes) -> can.Message:
        """
        Decrypting the can-message and bringing it into can.Message format
        :param message: messsage <bytes> received from arduino
        :return: can-message of format can.Message
        """
        message = message.decode()
        # can.Message(arbitration_id=message[], data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=True)
        return 0

    def sendCAN_Message(self, transmitter: CommunicationSerialArduino.sendSerialMessage, message: bytes) -> None:
        """
        Sending CAN-Message to Arduino
        :param transmitter: method of class CommunicationSerialArduino, that is responsible for sending data to Arduino Serial port
        :param message: message that shall be sent to arduino
        """
        transmitter(message)
