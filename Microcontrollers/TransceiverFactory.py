#!/usr/bin/env python3
# @author Markus Kösters


class TransceiverFactory:

    def __init__(self, device: type(callable)):
        self.device = device()

    def produceDevice(self):