#!/usr/bin/env python3
# @author Markus Kösters

import unittest

from BusTransactions import SerialBusConfig
from BusTransactions import SerialBus
from .SerialBusMock import MockSerialBus


class MyTestCase(unittest.TestCase):
    # print(MockBus)
    config = SerialBusConfig('test', 123, MockSerialBus)
    # print(config)
    bus = SerialBus(config)

    def test_write(self):
        testString = b'Hello World'
        self.bus.writeBus(testString)
        assert testString in self.bus.bus.getBuffer

    def test_read(self):
        testString = b'Hello World'
        self.bus.writeBus(testString)
        message = self.bus.readBus()
        assert message == testString


if __name__ == '__main__':
    unittest.main()
