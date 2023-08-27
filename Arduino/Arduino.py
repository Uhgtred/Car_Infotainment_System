#!/usr/bin/env python3
# @author      Markus Kösters

import serial

#from Configurations.ConfigReader import ConfigReader


class Arduino:

    device = None

    def __init__(self):
        #self.__conf: ConfigReader = ConfigReader()
        self.port: str = 'COM1' #self.__conf.readConfigParameter('ArduinoPort')
        self.baudRate: int = 9600 #int(self.__conf.readConfigParameter('ArduinoBaudRate'))
        self.delay: float = 0.5 #float(self.__conf.readConfigParameter('SerialTimeOut'))

    def close(self) -> None:
        if self.device.is_open:
            self.device.close()

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
        self.device = serial.Serial()
        self.device.baud = self.baudRate
        self.device.port = self.port
        if not self.device.is_open:
            self.device.open()
        self.device.delay = self.delay
        return self.device
