#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from BusTransactions import BusFactory, BusTransceiver
from BusTransactions import SerialBusConfig
from BusTransactions import SerialBus
from BusTransactions.Busses.SerialBusModule.UnitTests.test_SerialBus import MockBus
from BusTransactions import Encoding


class MyTestCase(unittest.TestCase):

    busFactory = BusFactory()
    bus = SerialBus
    mockLibrary = MockBus

    def test_produceBusTransceiver(self):
        config = SerialBusConfig('test', 123, self.mockLibrary)
        encoding = Encoding.EncodingContainer.arduinoSerialEncoding()
        transceiver = self.busFactory.produceBusTransceiver(config, encoding, SerialBus)
        assert isinstance(transceiver, BusTransceiver)


if __name__ == '__main__':
    unittest.main()
