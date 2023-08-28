#!/usr/bin/env python3
# @author: Markus Kösters
from abc import abstractmethod, ABC


class InterfaceEventManager(ABC):
    """
    Class for handling Events and notifying subscribers
    """

    @abstractmethod
    def subscribeToEvent(self, event: str, callbackMethod: any, moduleMainMethod) -> None:
        """
        Method for subscribing to
        """
        ...