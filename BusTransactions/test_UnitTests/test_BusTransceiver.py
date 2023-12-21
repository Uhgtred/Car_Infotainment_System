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
        """
        :TODO: make sure only one instance can read one message.
        :return:
        """
        # self.transceiver.writeSingleMessage(self.testString) # needed if only this method is tested.
        message = "none"
        # while message:
        print(self.transceiver.bus.bus.getBuffer)
        message = self.transceiver.readSingleMessage()
        print(self.transceiver.bus.bus.getBuffer)
        print(f'messsages received: {self.messages}')
        self.assertEqual(message, self.testString)
        # for message in self.messages:
        #     if self.testString in message:
        #         break
        # else:
        #     assert False
        # assert True


if __name__ == '__main__':
    unittest.main()
