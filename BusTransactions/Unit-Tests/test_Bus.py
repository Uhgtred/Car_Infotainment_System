import unittest
import serial

from BusTransactions.Bus import SerialBusArduino, BusConfig


class MyTestCase(unittest.TestCase):

    busConfig = BusConfig(serial.Serial, '/dev/ttyACM0', 115200)
    myBusClass = SerialBusArduino(busConfig)

    def test_canMakeArduinoSerialObject(self):
        bus = self.myBusClass.open()
        assert bus.is_open and type(bus) is serial.Serial

    def test_canCloseSerial(self):
        bus = self.myBusClass.open()
        if not bus.is_open:
            assert False
        bus.close()
        assert not bus.is_open

if __name__ == '__main__':
    unittest.main()
