#!/usr/bin/env python3
# @author Markus Kösters

import threading

from BusTransactions import BusFactory
from Events.EventInterface import EventInterface


class Main:
    """
    Main-program. Starts and organizes any submodules
    """

    def __init__(self):
        self.threads = Threads()

    @staticmethod
    def connectEvents() -> None:
        """
        Method for starting all events listed in the dictionary.
        """
        serialBusTransceiver = BusFactory.produceSerialTransceiver()
        EventInterface.subscribeToEvent(eventName='SerialBusEvent', callbackMethod=serialBusTransceiver.writeSingleMessage)


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
