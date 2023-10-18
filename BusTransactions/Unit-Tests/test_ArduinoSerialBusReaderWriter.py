import asyncio
import unittest

import serial

from BusTransactions import SerialBusArduino, SerialMessage
from BusTransactions.Bus import BusConfig
from Busses.BusReaderWriter import BusReaderWriterConfig, ArduinoSerialBusReaderWriter


class MyTestCase(unittest.TestCase):

    busConfig = BusConfig(serial.Serial, '/dev/ttyACM0', 115200)
    myBusClass = SerialBusArduino(busConfig)
    myBusReaderWriterConfig = BusReaderWriterConfig(myBusClass, SerialMessage())

    def test_canReadSingleMessage(self):
        busReaderWriter = ArduinoSerialBusReaderWriter(self.myBusReaderWriterConfig)
        message = busReaderWriter.read()
        assert message == 'TEST'

    def test_sendMessage(self):
        busReaderWriter = ArduinoSerialBusReaderWriter(self.myBusReaderWriterConfig)
        busReaderWriter.send('Hello World')
        assert busReaderWriter.read() == 'Hello World'

if __name__ == '__main__':
    unittest.main()
