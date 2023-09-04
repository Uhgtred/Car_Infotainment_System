#!/usr/bin/env python3
# @author: Markus Kösters

from typing import Protocol

from .InterfaceEventManager import InterfaceEventManager


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


class EventManager(InterfaceEventManager):
    """
    Class that is handling events.
    """

    # format of subscribers-list: {event:[subscribers]}
    __subscribedEvents = {str: list(str)}
    __eventProgramExit = ['all', 'exit']

    def subscribeToEvent(self, event: Event) -> None:
        """
        Method for registering event-callbackMethod to a specified event
        :param event: Object of type class Event, with attributes: name: str and subscribeTo: str
        """
        # checks if eventName is already in dict and returns it,
        # else sets it as key and empty list as value
        subscribedEventList = self.__subscribedEvents.setdefault(event.subscribeTo, [])
        if event.name not in subscribedEventList:
            subscribedEventList.append(event.name)

    def __notifySubscribers(self, eventName: Event.name, message: any) -> None:
        """
        Notifying the registered processes of the specified event.
        :param eventName: Name of the event used for identification.
        :param message: Data that shall be passed to the receiveEventUpdate-method of subscribed event.
        """
        #
        subscribedCallbacksList = self.__subscribedEvents.get(eventName)
        for subscriber in subscribedCallbacksList:
            subscriber.receiveEventUpdate(message)

