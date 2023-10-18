#!/usr/bin/env python3
# @author: Markus Kösters
from dataclasses import dataclass


class SerialBusConfig(dataclass):
    """
    Config-dataclass for Serial-busses.
    """
    port: str
    baudRate: int
