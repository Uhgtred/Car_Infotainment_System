import unittest

from Microcontrollers import SerialMessage


class MyTestCase(unittest.TestCase):

    serialMessageFormatter = SerialMessage()

    def test_canEncodeMessage(self):
        text = 'Hello World'
        assert self.serialMessageFormatter.encodeMessage(text) == f'{text}&'.encode()

    def test_canDecodeMessage(self):
        text = b'Hello World&'
        assert self.serialMessageFormatter.decodeMessage(text) == text.decode().removesuffix('&')


if __name__ == '__main__':
    unittest.main()
