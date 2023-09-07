#!/usr/bin/env python3
# @author: Markus Kösters
import this
from abc import abstractmethod, ABC

from .Event import Event


class InterfaceEventManager(ABC):
    """
    Class for handling Events and notifying subscribers
    """

    @abstractmethod
    def subscribeToEvent(self, subscriber: Event, event: Event) -> None:
        """
        Method for registering a process to the Event-Manager.
        :param subscriber: Object of the class that going to be subscribed.
        :param event: Name of the event that is going to be subscribed to.
        """
        ...

    @abstractmethod
    def unsubscribeFromEvent(self, subscriber: Event, event: Event) -> None:
        """
        Method for unsubscribing an event from the Event-Manager.
        """

    @abstractmethod
    def postEventUpdate(self, event: str, data: any) -> None:
        """
        Method for posting an Event-Update to Event-Manager.
        """
