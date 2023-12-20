#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from BusTransactions import BusInterfaceFactory, SerialBus, SerialBusConfig
from BusTransactions.Buses.SerialBusModule.test_UnitTests.SerialBusMock import MockSerialBus
from BusTransactions.Encoding import EncodingFactory


class MyTestCase(unittest.TestCase):

    transceiver = BusInterfaceFactory()
    config = SerialBusConfig('test', 123, MockSerialBus)
    bus = SerialBus(config)
    transceiver = transceiver.produceBusTransceiver(bus, EncodingFactory.arduinoSerialEncoding)
    testString = 'Test from BusTransceiver'

    def test_BusTransceiver_writeSingleMessage(self):
        self.transceiver.writeSingleMessage(self.testString)
        assert self.testString.encode() in self.transceiver.bus.bus.getBuffer[0]

    def test_BusTransceiver_readSingleMessage(self):
        self.transceiver.writeSingleMessage(self.testString)
        message = self.transceiver.readSingleMessage()
        assert self.testString in message

if __name__ == '__main__':
    unittest.main()