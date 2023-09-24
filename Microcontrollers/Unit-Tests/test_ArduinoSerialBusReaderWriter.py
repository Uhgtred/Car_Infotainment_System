import asyncio
import unittest

import serial

from Microcontrollers import SerialBusArduino, SerialMessage
from Microcontrollers.Bus import BusConfig
from Microcontrollers.BusReaderWriter import BusReaderWriterConfig, ArduinoSerialBusReaderWriter


class MyTestCase(unittest.TestCase):

    busConfig = BusConfig(serial.Serial, '/dev/ttyACM0', 115200)
    myBusClass = SerialBusArduino(busConfig)
    myBusReaderWriterConfig = BusReaderWriterConfig(myBusClass, SerialMessage)

    def test_readBus(self):
        busReaderWriter = ArduinoSerialBusReaderWriter(self.myBusReaderWriterConfig)
        busReaderWriter.send('TEST')

    def callbackMethod(self, message):
        print(f'Message: {message}')
        assert type(message) is bytes

    def test_canReadSingleMessage(self):
        self.communicationClassObject.read(self.callbackMethod)

    def test_sendMessage(self):
        self.communicationClassObject.send(SerialMessage().encodeMessage('Hello World'))

if __name__ == '__main__':
    unittest.main()
