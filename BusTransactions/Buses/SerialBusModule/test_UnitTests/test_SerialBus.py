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
    testString = b'Hello World'

    def test_write(self):
        self.bus.writeBus(self.testString)
        assert self.testString in self.bus.bus.getBuffer

    def test_read(self):
        # self.bus.writeBus(testString) # needed when only this method is tested
        message = self.bus.readBus()
        assert message == self.testString


if __name__ == '__main__':
    unittest.main()
