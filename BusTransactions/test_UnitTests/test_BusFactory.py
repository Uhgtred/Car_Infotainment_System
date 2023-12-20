#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from BusTransactions import BusInterfaceFactory, BusInterface
from BusTransactions import SerialBus
from BusTransactions.Buses.SerialBusModule.test_UnitTests.SerialBusMock import MockSerialBus


class MyTestCase(unittest.TestCase):

    busFactory = BusInterfaceFactory()
    bus = SerialBus
    mockLibrary = MockSerialBus

    def test_produceBusTransceiver(self):
        """TODO: code is not testable. Check architecture for quality."""
        pass
        # transceivers = []
        # for method in dir(self.busFactory):
        #     if not method.startswith("__"):
        #         transceiver = getattr(self.busFactory, method)()
        #         transceivers.append(transceiver)
        # for transceiver in transceivers:
        #     assert isinstance(transceiver, BusInterface)


if __name__ == '__main__':
    unittest.main()
