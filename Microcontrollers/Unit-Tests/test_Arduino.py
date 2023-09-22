import unittest
import serial

from Microcontrollers.Bus import SerialBusArduino


class MyTestCase(unittest.TestCase):

    arduinoClassObject = SerialBusArduino()

    def test_canMakeArduinoObject(self):
        arduino = self.arduinoClassObject.open()
        assert arduino.is_open and type(arduino) is serial.Serial

    def test_canCloseSerial(self):
        arduino = self.arduinoClassObject.open()
        if not arduino.is_open:
            assert False
        arduino.close()
        assert not arduino.is_open

    def test_canGetPort(self):
        assert self.arduinoClassObject.port == '/dev/ttyACM0'


if __name__ == '__main__':
    unittest.main()
