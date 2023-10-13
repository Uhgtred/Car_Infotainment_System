#!/usr/bin/env python3
# @author: Markus Kösters

from abc import ABC, abstractmethod


class EventUpdater(ABC):
    """
    Protocol to prescribe the structure of an Event.
    """

    @abstractmethod
    def receiveEventUpdate(self, callbackMethod: callable, frequency: int) -> None:
        """
        Method that receives notifications for subscribers.
        :param callbackMethod: EventManager.postEventUpdate, sending updates to all subscribers
        :param frequency: how many times a second shall the update be pulled?
        """
        ...
