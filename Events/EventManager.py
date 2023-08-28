#!/usr/bin/env python3
# @author: Markus Kösters
import multiprocessing

from Processes import ProcessManager
from .EventReceiver import EventReceiver
from .InterfaceEventManager import InterfaceEventManager


class EventManager(InterfaceEventManager):
    __eventPipes = []
    __subscribers = {}

    def __init__(self):
        self.eventReceiver = EventReceiver()
        self.processManager = ProcessManager()

    def subscribeToEvent(self, event: str, callbackMethod: any, moduleMainMethod) -> None:
        """
        Adding the event to subscribers-dictionary if not yet in there.
        :param event: string representing the event that shall be subscribed to
        :param callbackMethod: method that shall be called on event
        """
        if event not in self.__subscribers:
            self.__subscribers[event] = []
        if callbackMethod not in self.__subscribers[event]:
            parentPipe, childPipe = multiprocessing.Pipe()
            callBackData = (parentPipe, callbackMethod)
            self.processManager.openSubprocess(moduleMainMethod, childPipe)
            # adding a tuple of data to the dictionary containing the subscribers data
            self.__subscribers[event].append(callBackData)

    def __notifySubscribers(self, event: str, message: any):
        for subscriber in self.__subscribers:
            if subscriber[0] == event:
                # sending the method that is to be executed and the message provided to that method
                subscriber[0].send((subscriber[1], message))
