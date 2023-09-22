#!/usr/bin/env python3
# @author Markus Kösters
import serial

from Microcontrollers import SerialBusArduino, BusReaderWriter, Message, SerialMessage
from Microcontrollers.Bus import BusConfig, Bus
from Microcontrollers.BusReaderWriter import BusReaderWriterConfig
from Microcontrollers.Transceiver import Transceiver, TransceiverConfig


class TransceiverFactory:
    """
    Factory for the Transceiver communicating with MicroController bus-systems.
    TODO: Finish implementation. This is just a prototype!
    """

    def initBus(self) -> Bus:
        busControllerConfig = BusConfig(serial.Serial, '/dev/ttyACM0', 115200)
        bus = SerialBusArduino(busControllerConfig)
        return bus

    def initBusReaderWriter(self) -> BusReaderWriter:
        busReaderWriterConfig = BusReaderWriterConfig(self.initBus(), SerialMessage())
        busReaderWriter = BusReaderWriter(busReaderWriterConfig)
        return busReaderWriter

    def initTransceiver(self) -> Transceiver:
        transceiverConfig = TransceiverConfig(self.initBus(), SerialMessage(), self.initBusReaderWriter())
        transceiver = Transceiver(transceiverConfig)
        return transceiver
