import unittest
import serial

from Arduino import ArduinoConnector


class MyTestCase(unittest.TestCase):

    arduinoClassObject = ArduinoConnector()

    def test_canMakeArduinoObject(self):
        arduino = self.arduinoClassObject.arduino
        assert arduino.is_open and type(arduino) is serial.Serial

    def test_canCloseSerial(self):
        arduino = self.arduinoClassObject.arduino
        if not arduino.is_open:
            assert False
        arduino.close()
        assert not arduino.is_open


if __name__ == '__main__':
    unittest.main()
