#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from BusTransactions import BusFactory, SerialBus, SerialBusConfig
from BusTransactions.Busses.SerialBusModule.UnitTests.test_SerialBus import MockBus
from BusTransactions.Encoding import Encoding


class MyTestCase(unittest.TestCase):

    transceiver = BusFactory()
    config = SerialBusConfig('test', 123, MockBus)
    transceiver = transceiver.produceBusTransceiver(config, Encoding.EncodingContainer.arduinoSerialEncoding(), SerialBus)

    def test_BusTransceiver_writeSingleMessage(self):
        self.transceiver.writeSingleMessage()

    def test_BusTransceiver_readSingleMessage(self):

        self.transceiver.readSingleMessage()

if __name__ == '__main__':
    unittest.main()