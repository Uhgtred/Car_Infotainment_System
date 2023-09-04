#!/usr/bin/env python3
# @author: Markus Kösters
import this
from abc import abstractmethod, ABC

from Events.EventManager import Event


class InterfaceEventManager(ABC):
    """
    Class for handling Events and notifying subscribers
    """

    @abstractmethod
    def subscribeToEvent(self, eventName: Event.subscribeTo) -> None:
        """
        Method for registering a process to the eventhandler
        """
        ...
