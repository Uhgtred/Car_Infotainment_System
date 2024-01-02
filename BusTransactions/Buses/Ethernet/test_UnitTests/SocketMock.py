#!/usr/bin/env python3
# @author: Markus Kösters

class MockSocket:
    buffer = []
    state = False

    def read(self):
        if self.buffer:
            return self.buffer.pop(0)

    def socket(self):
        if self.state:
            self.state = True
        else:
            self.state = False

    def write(self, message):
        self.buffer.append(message)

    @property
    def getBuffer(self):
        return self.buffer
