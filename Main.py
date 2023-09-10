#!/usr/bin/env python3
# @author Markus Kösters
import threading

from Events.Event import CAN_TransceiverEvent
from Events.EventFactory import EventConnectionFactory, EventObjectFactory


class Main:
    """
    Main-program. Starts and organizes any submodules
    """
    __events = [CAN_TransceiverEvent]

    def __init__(self):
        self.threads = Threads()

    def connectEvent(self) -> None:
        """
        Method for starting an event
        """
        for event in self.__events:
            eventConnector = event()
            self.threads.startMethodInThread(eventConnector.setupEvent)



class Threads:


    __threads: dict = {}

    @staticmethod
    def threadName(method: callable) -> str:
        """
        TODO: create a functionality to decode the name of the method into a threadname
        Method for creating a name for the thread that is about to be started.
        """

        return 'ThreadName'

    def startMethodInThread(self, method: callable, *args) -> None:
        """
        Method for running a passed method in a new thread.
        :param method: Method that shall be executed in a separate thread.
        :param args: Arguments, that shall be passed to the thread.
        """
        threadName = self.threadName(method)
        thread = threading.Thread(target=method, args=[*args], name=threadName)
        self.__threads[threadName] = thread
        thread.start()
