#!/usr/bin/env python3
# @author      Markus Kösters

from typing import Protocol


class Event(Protocol):
    """
    Protocol for prescribing the structure of a concrete Event.
    """
    name: str
    subscribeTo: str

    def setupEvent(self) -> None:
        """
        Method for configuring the concrete Event.
        """
        ...

    def receiveEventUpdate(self, data: any) -> None:
        """
        Method for receiving updates from the subscribed event.
        :param data: Data that shall be received from the subscribed event.
        """
        ...

    def postEventUpdate(self, data: any) -> None:
        """
        Method for posting event-updates to the Event-Manager.
        :param data: Data that shall be shared with the subscribers.
        """
        ...
