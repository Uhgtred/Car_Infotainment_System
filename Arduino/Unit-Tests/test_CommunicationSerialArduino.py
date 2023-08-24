import asyncio
import unittest

from Arduino import CommunicationSerialArduino


class MyTestCase(unittest.TestCase):

    communicationClassObject = CommunicationSerialArduino()

    def test_canHookMessageLoop(self):
        self.communicationClassObject.linkSerialReadLoopToNotification(self.getNotified)

    def getNotified(self, message):
        print(f'Message: {message}')
        assert type(message) is bytes

    def test_sendMessage(self):
        asyncio.run(self.communicationClassObject.sendSerialMessage(b'Hello World'))

if __name__ == '__main__':
    unittest.main()
