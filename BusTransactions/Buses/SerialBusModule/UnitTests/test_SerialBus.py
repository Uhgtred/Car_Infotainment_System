#!/usr/bin/env python3
# @author Markus Kösters

import unittest

from BusTransactions.Buses.SerialBusModule import SerialBusConfig, SerialBus


class MockBus:
    buffer = []
    state = False

    def read(self):
        if self.buffer:
            return self.buffer.pop(0)

    def write(self, message):
        self.buffer.append(message)

    def isOpen(self):
        return self.state

    def open(self):
        self.state = True

    def close(self):
        self.state = False

    @property
    def getBuffer(self):
        return self.buffer


class MyTestCase(unittest.TestCase):
    # print(MockBus)
    config = SerialBusConfig('test', 123, MockBus)
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
