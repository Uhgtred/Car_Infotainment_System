#!/usr/bin/env python3
# @author Markus Kösters
import threading
import time
from typing import TypedDict, Type

from Events import EventFactory
from Microcontrollers.InterfaceTransceiver import Transceiver


class EventDictionary(TypedDict):
    module: Type[any]
    name: str
    subscribeTo: str


class Main:
    """
    Main-program. Starts and organizes any submodules
    """
    # TODO: put this list into a confi-file with json-format.
    __events: list[[callable]] = [[Transceiver().sendMessage]]

    def __init__(self):
        self.threads = Threads()

    def connectEvents(self) -> None:
        """
        Method for starting all events listed in the dictionary.
        """
        for eventUserList in self.__events:
            eventObject = EventFactory.ProduceEventUser()
            for eventUser in eventUserList:
                eventObject.subscribeToEvent(eventUser)

class Threads:
    """
    Method for organizing threads and keeping track of opened tracks.
    TODO: implement a method that closes any running threads on program-exit
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
