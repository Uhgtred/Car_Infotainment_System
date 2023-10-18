#!/usr/bin/env python3
# @author Markus Kösters

from dataclasses import dataclass

from Microcontrollers import Message


@dataclass
class TransceiverConfig:
    # method of the bus-object that is responsible for sending messages to the bus
    sendMessage: callable
    # method of the bus-object that is responsible for receiving messages from the bus
    readMessage: callable


class Transceiver:

    def __init__(self, config: TransceiverConfig):
        self.__config = config

    def sendMessage(self, message: Message):
        self.__config.sendMessage(message)
