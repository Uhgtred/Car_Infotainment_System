import unittest

import serial

from Microcontrollers import SerialMessage
from Microcontrollers.Bus import BusConfig, SerialBusArduino
from Microcontrollers.BusReaderWriter import BusReaderWriterConfig, BusReaderWriter
from Microcontrollers.InterfaceTransceiver import Transceiver, TransceiverConfig


class MyTestCase(unittest.TestCase):

    busConfig = BusConfig(serial.Serial, '/dev/ttyACM0', 115200)
    bus = SerialBusArduino(busConfig)
    busReaderWriterConfig = BusReaderWriterConfig(bus, SerialMessage())
    busReaderWriter = BusReaderWriter(busReaderWriterConfig)
    transceiverConfig = TransceiverConfig(bus, busReaderWriter, 'TEST')
    transceiver = Transceiver(transceiverConfig)

    def test_receiveMessageLooped(self):
        self.transceiver.receiveMessage(self.callbackMethod)

    def test_receiveMessageNonLooped(self):
        self.transceiver.receiveMessage(self.callbackMethod, loop=False)

    def callbackMethod(self, message):
        assert message == 'Hello World'

    def test_canSendMessage(self):
        message = 'Hello World'
        self.transceiver.sendMessage(message)
        self.transceiver.receiveMessage(self.callbackMethod, loop=False)


if __name__ == '__main__':
    unittest.main()
