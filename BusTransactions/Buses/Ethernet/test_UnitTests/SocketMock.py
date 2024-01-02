#!/usr/bin/env python3
# @author: Markus Kösters

class MockSocket:
    buffer = []

    def __init__(self, config):
        pass

    def read(self):
        if self.buffer:
            return self.buffer.pop(0)

    def write(self, message):
        self.buffer.append(message)

    @property
    def getBuffer(self):
        return self.buffer
