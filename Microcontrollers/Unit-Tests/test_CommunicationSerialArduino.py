import asyncio
import unittest

from Arduino import ArduinoSerialBus


class MyTestCase(unittest.TestCase):

    communicationClassObject = ArduinoSerialBus()

    def test_canHookMessageLoop(self):
        self.communicationClassObject.subscribeSerialReadLoop(self.getNotified)

    def getNotified(self, message):
        print(f'Message: {message}')
        assert type(message) is bytes

    def test_sendMessage(self):
        asyncio.run(self.communicationClassObject.sendSerialMessage(b'Hello World'))

if __name__ == '__main__':
    unittest.main()
