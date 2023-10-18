#!/usr/bin/env python3
# @author Markus Kösters

from abc import ABC, abstractmethod


class DeviceInterface(ABC):

    @abstractmethod
    def read(self):
