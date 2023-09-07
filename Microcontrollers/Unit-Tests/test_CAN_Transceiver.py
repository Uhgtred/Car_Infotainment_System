import unittest

from Microcontrollers.Transceiver import CAN_Transceiver


class MyTestCase(unittest.TestCase):

    transceiver = CAN_Transceiver()

    def test_receiveMessageLooped(self):
        self.transceiver.receiveMessage(self.callbackMethod)

    def test_receiveMessageNonLooped(self):
        self.transceiver.receiveMessage(self.callbackMethod)

    def callbackMethod(self, message):
        assert message == 'Hello World'

    def test_canSendMessage(self):
        message = 'Hello World'
        self.transceiver.sendMessage(message)


if __name__ == '__main__':
    unittest.main()
