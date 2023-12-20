#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from BusTransactions import BusInterfaceFactory, SerialBus, SerialBusConfig
from BusTransactions.Buses.SerialBusModule.test_UnitTests.test_SerialBus import MockBus
from BusTransactions.Encoding import EncodingInterface


class MyTestCase(unittest.TestCase):

    transceiver = BusInterfaceFactory()
    config = SerialBusConfig('test', 123, MockBus)
    transceiver = transceiver.produceBusTransceiver(config, Encoding.EncodingInterface.arduinoSerialEncoding, SerialBus)
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