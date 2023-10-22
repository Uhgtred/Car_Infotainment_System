#!/usr/bin/env python3
# @author: Markus Kösters

from abc import ABC, abstractmethod


class EventUser(ABC):
    """
    Protocol to prescribe the structure of an Event.
    """

    @abstractmethod
    def subscribeToEvent(self, eventCallbackMethod: callable) -> None:
        """
        Method for returning event-updates to a callbackMethod.
        """
        pass

    @abstractmethod
    def postEventUpdate(self, data: any) -> None:
        """
        Method to send an event-update to a subscriber.
        :param data: data that shall be received by this method from EventManager.
        """
        pass
