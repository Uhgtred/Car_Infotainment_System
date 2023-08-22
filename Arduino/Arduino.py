#!/usr/bin/env python3
# @author      Markus Kösters

import serial

from Configurations.ConfigReader import ConfigReader


class Arduino:

    def __init__(self):
        self.__conf: ConfigReader = ConfigReader()
        self.port: str = self.__conf.readConfigParameter('ArduinoPort')
        self.baudRate: int = int(self.__conf.readConfigParameter('ArduinoBaudRate'))
        self.delay: float = float(self.__conf.readConfigParameter('SerialTimeOut'))

    @staticmethod
    def close(arduino: serial.Serial) -> None:
        if arduino.is_open():
            arduino.close()

    @property
    def arduino(self) -> serial.Serial:
        """
        Returning an object of the microcontroller to interact with.
        Make sure to call the method: close(arduino) when you are done
        :return: connection-object to microcontroller
        """
        return self.initArduino()

    def initArduino(self) -> serial.Serial:
        """
        Initializing the microcontroller and opening connection to it.
        :return: object of a microcontroller-instance
        """
        device = serial.Serial()
        device.baud = self.baudRate
        device.port = self.port
        if not device.is_open():
            device.open()
        device.delay = self.delay
        return device
