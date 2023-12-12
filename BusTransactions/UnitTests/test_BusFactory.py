#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from BusTransactions import BusInterfaceFactory, BusInterface
from BusTransactions import SerialBusConfig
from BusTransactions import SerialBus
from BusTransactions.Buses.SerialBusModule.UnitTests.test_SerialBus import MockBus
from BusTransactions import Encoding


class MyTestCase(unittest.TestCase):

    busFactory = BusInterfaceFactory()
    bus = SerialBus
    mockLibrary = MockBus

    def test_produceBusTransceiver(self):
        config = SerialBusConfig('test', 123, self.mockLibrary)
        encoding = Encoding.EncodingInterface.arduinoSerialEncoding()
        transceiver = self.busFactory.produceBusTransceiver(config, encoding, SerialBus)
        print(transceiver)
        assert isinstance(transceiver, BusInterface)


if __name__ == '__main__':
    unittest.main()
