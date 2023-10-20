#!/usr/bin/env python3
# @author Markus Kösters

import unittest

from BusTransactions.Busses.SerialBus.SerialBusConfig import SerialBusConfig


class MockBus:
    def __init__(self, config: SerialBusConfig):
        self.config = config

    def readBus(self) -> bytes:
        """
        Interface-method for reading from a bus.
        :return: Bytes containing the message.
        """
        return f'Reading message from: {self.config}'.encode()

    def writeBus(self, message: bytes) -> None:
        """
        Interface-method for writing to a bus.
        :param message: Message that shall be sent to the bus.
        """
        pass


class MyTestCase(unittest.TestCase):
    config = SerialBusConfig(MockBus, 'test', 123)

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
