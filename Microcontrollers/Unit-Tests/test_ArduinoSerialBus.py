import asyncio
import unittest

from Microcontrollers import ArduinoSerialBus, Arduino, SerialMessage


class MyTestCase(unittest.TestCase):

    communicationClassObject = ArduinoSerialBus(Arduino().open())

    def test_canHookMessageLoop(self):
        self.communicationClassObject.readLoop(self.callbackMethod)

    def callbackMethod(self, message):
        print(f'Message: {message}')
        assert type(message) is bytes

    def test_canReadSingleMessage(self):
        self.communicationClassObject.read(self.callbackMethod)

    def test_sendMessage(self):
        self.communicationClassObject.send(SerialMessage().encodeMessage('Hello World'))

if __name__ == '__main__':
    unittest.main()