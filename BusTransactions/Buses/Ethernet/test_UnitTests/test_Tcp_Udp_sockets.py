#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from BusTransactions.Buses.Ethernet import SocketConfigs, Tcp_Udp_sockets
from BusTransactions.Buses.Ethernet.test_UnitTests import SocketMock


class MyTestCase(unittest.TestCase):
    # print(MockBus)
    config = SocketConfigs.UdpSocketConfig(1234, 'test.test.test.test', SocketMock)
    # print(config)
    bus = Tcp_Udp_sockets.UdpSocket(config)
    testString = b'Hello World'

    def test_write(self):
        self.bus.writeBus(self.testString)
        message = self.bus.bus.buffer.pop(0)
        self.assertEqual(message, self.testString)

    def test_read(self):
        self.bus.writeBus(self.testString)
        message = self.bus.readBus()
        assert message == self.testString


if __name__ == '__main__':
    unittest.main()
