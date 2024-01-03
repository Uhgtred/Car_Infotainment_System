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

    @classmethod
    def socket(cls, *args):
        if cls.state:
            cls.state = True
        else:
            cls.state = False

    def sendto(self, message, ):
        self.buffer.append(message)

    @property
    def getBuffer(self):
        return self.buffer
