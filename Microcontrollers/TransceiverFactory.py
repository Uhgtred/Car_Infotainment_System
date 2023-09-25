#!/usr/bin/env python3
# @author Markus Kösters
import serial

from Microcontrollers import SerialBusArduino, BusReaderWriter, SerialMessage, Message
from Microcontrollers.Bus import BusConfig, Bus
from Microcontrollers.BusReaderWriter import BusReaderWriterConfig
from Microcontrollers.InterfaceTransceiver import InterfaceTransceiver, TransceiverConfig


class TransceiverFactory:
    """
    Factory for the Transceiver communicating with MicroController bus-systems.
    TODO: Finish implementation. This is just a prototype!
    """
    busType = serial.Serial

    def produceBus(self, concreteBusClass: type(Bus), busType: any, port: str, frequency: int) -> Bus:
        """
        Producing a bus-interface-object.
        :param concreteBusClass: Concrete class that implements the abstraction.
        :param busType: Type of bus that shall be opened, e.g. serial.Serial.
        :param port: <string> representing the port of the connected bus
                    (E.g. for Serial and Linux: '/dev/ttyACM0'
                        for Serial and Windows: 'COM1').
        :param frequency: <int> setting the frequency (for Serial baud-rate) of the bus.
        :return: interface-object for the bus.
        """
        busControllerConfig = concreteBusClass(busType, port, frequency)
        bus = SerialBusArduino(busControllerConfig)
        return bus

    def produceBusReaderWriter(self, concreteReaderWriterClass: type(BusReaderWriter), messageType: Message, concreteBusClass: type(Bus), busType: any, port: str, frequency: int) -> BusReaderWriter:
        """
        Produce bus-reader-writer, accessing a bus-interface-object and reading from/writing to the bus.
        :param frequency: <int> setting the frequency (for Serial baud-rate) of the bus.
        :param port: <string> representing the port of the connected bus
                    (E.g. for Serial and Linux: '/dev/ttyACM0'
                        for Serial and Windows: 'COM1').
        :param busType: Type of bus that shall be opened, e.g. serial.Serial.
        :param concreteBusClass: Concrete class that implements the abstraction.
        :param concreteReaderWriterClass: Concrete class that implements the abstraction.
        :param messageType: <Message> message-object setting the protocol of message for matching the protocol of the bus.
        :return: interface-object for the read-writer of the bus.
        """
        bus = self.produceBus(concreteBusClass, busType, port, frequency)
        busReaderWriterConfig = concreteReaderWriterClass(bus, messageType)
        busReaderWriter = BusReaderWriter(busReaderWriterConfig)
        return busReaderWriter

    def produceTransceiver(self, eventName: str, concreteTransceiverClass: type(InterfaceTransceiver), concreteReaderWriterClass: type(BusReaderWriter), messageType: Message, concreteBusClass: type(Bus), busType: any, port: str, frequency: int) -> InterfaceTransceiver:
        """
        Produce Transceiver for a bus, managing any underlying mechanisms, so that a simple string can be pushed to this function,
        which is then being converted/encoded before sending to the bus. Also implements support for constantly receiving from a bus in a loop.
        :TODO: find some other way to do subscription then eventName. This is not good!
        :param eventName: Name that eventManager can use to subscribe other methods.
        :param concreteTransceiverClass: Concrete class that implements the abstraction.
        :param frequency: <int> setting the frequency (for Serial baud-rate) of the bus.
        :param port: <string> representing the port of the connected bus
                    (E.g. for Serial and Linux: '/dev/ttyACM0'
                        for Serial and Windows: 'COM1').
        :param busType: Type of bus that shall be opened, e.g. serial.Serial.
        :param concreteBusClass: Concrete class that implements the abstraction.
        :param concreteReaderWriterClass: Concrete class that implements the abstraction.
        :param messageType: <Message> message-object setting the protocol of message for matching the protocol of the bus.
        :return: interface-object for handling any communication with a specified bus.
        """
        bus = self.produceBus(concreteBusClass, busType, port, frequency)
        readerWriter = self.produceBusReaderWriter(concreteReaderWriterClass, messageType, concreteBusClass, busType, port, frequency)
        transceiverConfig = TransceiverConfig(bus, readerWriter, eventName)
        transceiver = concreteTransceiverClass(transceiverConfig)
        return transceiver
