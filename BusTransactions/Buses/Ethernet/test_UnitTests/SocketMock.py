#!/usr/bin/env python3
# @author: Markus Kösters

class MockSocket:
    buffer = []
    state = False
    AF_INET = None
    SOCK_STREAM = None
    SOCK_DGRAM = None

    def read(self):
        if self.buffer:
            return self.buffer.pop(0)

    @staticmethod
    def bind(address):
        print(f'Address of socket: {address}')

    @classmethod
    def socket(cls, *args):
        if cls.state:
            cls.state = True
        else:
            cls.state = False
        return cls

    @classmethod
    def sendto(cls, message, address):
        print(f'Sending message: {message} to socket: {address}')
        cls.buffer.append(message)

    @property
    def getBuffer(self):
        return self.buffer
