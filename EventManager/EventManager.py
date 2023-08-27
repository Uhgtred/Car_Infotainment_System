#!/usr/bin/env python3
# @author: Markus Kösters
import multiprocessing

from .InterfaceEventManager import InterfaceEventManager


class EventManager(InterfaceEventManager):
    __eventNotifierQueue = multiprocessing.Queue()
    __eventSubscriberQueue = multiprocessing.Queue()

    @property
    def eventNotifierQueue(self):
        """
        Getter for eventNotifierQueue, which manages event-updates from
        notifiers on external processes to EventManager.
        """
        return self.__eventNotifierQueue

    @property
    def eventSubscriberQueue(self):
        """
        Getter for eventQueue, which manages event-updates to
        subscribers on external processes, from EventManager.
        """
        return self.__eventNotifierQueue
