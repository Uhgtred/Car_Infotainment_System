#!/usr/bin/env python3
# @author: Markus Kösters
import time
import unittest

from BusTransactions import BusInterfaceFactory, SerialBus, SerialBusConfig
from BusTransactions.Buses.SerialBusModule.test_UnitTests.SerialBusMock import MockSerialBus
from BusTransactions import Encoding


class MyTestCase(unittest.TestCase):
    transceiver = BusInterfaceFactory()
    config = SerialBusConfig('test', 123, MockSerialBus)
    bus = SerialBus(config)
    transceiver = transceiver.produceBusTransceiver(bus, Encoding.EncodingFactory.arduinoSerialEncoding)
    testString = 'Test from BusTransceiver'
    messages = []

    def test_BusTransceiver_writeSingleMessage(self):
        self.transceiver.writeSingleMessage(self.testString)
        buffer = self.transceiver.bus.bus.getBuffer
        for message in buffer:
            if self.testString.encode() in message:
                break
        else:
            assert False
        assert True

    def test_BusTransceiver_readSingleMessage(self):
        self.transceiver.writeSingleMessage(self.testString)
        self.messages.append(str(self.transceiver.readSingleMessage()))
        print(self.messages)
        for message in self.messages:
            if self.testString in message:
                break
        else:
            assert False
        assert True


if __name__ == '__main__':
    unittest.main()
