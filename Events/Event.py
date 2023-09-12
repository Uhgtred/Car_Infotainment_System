#!/usr/bin/env python3
# @author: Markus Kösters

from typing import Protocol


class Event(Protocol):
    """
    Protocol to prescribe the structure of an Event.
    """

    def sendMessage(self, callbackMethod: callable, loop: bool = True) -> None:
        """
        Method that sends messages to a subscribed method.
        :param callbackMethod: EventManager.postEventUpdate, sending updates to all subscribers
        :param loop: making the method send messages in a loop.
        """
        ...

    def receiveMessage(self, data: any) -> None:
        """
        Method to receive an event-update from a subscription.
        :param data: data that shall be received by this method from EventManager.
        """
        ...
