#!/usr/bin/env python3
# @author      Markus Kösters

import atexit
from abc import abstractmethod, ABC
from typing import NamedTuple

from .Message import Message
from .Bus import Bus


class BusReaderWriterConfig(NamedTuple):
    bus: Bus
    messageType: Message


class BusReaderWriter(ABC):
    """
    Class for prescribing the structure of how to build a bus-connection.
    """

    def __init__(self, config: BusReaderWriterConfig):
        self.config = config

    @abstractmethod
    def read(self) -> any:
        """
        Method for reading a single message from a Bus.
        """
        ...

    @abstractmethod
    def send(self, message: Message.encodeMessage) -> None:
        """
        Method for properly closing a connection to a Microcontroller.
        :param message: Message that shall be sent to the bus
        """
        ...


class ArduinoSerialBusReaderWriter(BusReaderWriter):
    """
    Class for async Serial-communication with arduino
    """

    def __init__(self, config: BusReaderWriterConfig):
        super().__init__(config)
        self.config.bus = config.bus.open()
        # Close serial connection, when program closes
        atexit.register(self.exitHandler)

    def read(self) -> bytes:
        """
        Read a single Serial-Message from the bus.
        :return: Message read from the bus in bytes-format.
        """
        return self.config.bus.readline()

    def send(self, message: str | bytes) -> None:
        """
        Sending a message to the microcontroller.
        :param message: Message that is to be sent to the bus.
        """
        self.config.bus.write(self.config.messageType.encodeMessage(message))

    def exitHandler(self) -> None:
        """
        Closing the Serial-connection at exit.
        """
        try:
            self.config.bus.close()
        except Exception as e:
            raise Exception(f'Error while trying to close Arduino: {e}')
