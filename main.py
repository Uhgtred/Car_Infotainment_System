#!/usr/bin/env python3
# @author Markus Kösters

import threading
from typing import TypedDict, Type

from BusTransactions import BusFactory
from BusTransactions.Buses import SerialBus
from BusTransactions.Buses.SerialBusModule.SerialBusConfig import SerialBusConfig
from BusTransactions.Encoding import EncodingInterface
from Events import EventFactory


class EventDictionary(TypedDict):
    module: Type[any]
    name: str
    subscribeTo: str


class Main:
    """
    Main-program. Starts and organizes any submodules
    """
    # :TODO: put this list into a config-file with json-format.
    serialBusSetup = [SerialBusConfig, EncodingInterface.arduinoSerialEncoding]
    # :END TODO:
    __factoryConfigs: dict[[callable]] = {'serialBusArduino': [serialBusSetup]}
    __eventObjects: dict[str, object] = {}

    def __init__(self):
        self.threads = Threads()

    def connectEvents(self) -> None:
        """
        Method for starting all events listed in the dictionary.
        """
        eventObject = EventFactory.EventFactory.produceEventUser()
        serialBusTransceiver = BusFactory.produceSerialTransceiver(*self.__factoryConfigs.get('serialBusArduino'))
        eventObject.subscribeToEvent(serialBusTransceiver.writeSingleMessage)
        self.__eventObjects['serialBusTransmitterArduino'] = eventObject


class Threads:
    """
    Method for organizing threads and keeping track of opened tracks.
    """

    __threads: dict = {}

    def startMethodInThread(self, method: callable, threadName: str, *args) -> None:
        """
        Method for running a passed method in a new thread.
        :param threadName: Name for the thread for easier identification.
        :param method: Method that shall be executed in a separate thread.
        :param args: Arguments, that shall be passed to the thread.
        """
        args = list(*args)
        thread = threading.Thread(target=method, args=args, name=threadName)
        self.__threads[threadName] = thread
        thread.start()


if __name__ == '__main__':
    main = Main()
    main.connectEvents()
