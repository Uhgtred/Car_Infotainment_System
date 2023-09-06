#!/usr/bin/env python3
# @author: Markus Kösters

from typing import TypedDict

from .Event import Event
from .InterfaceEventManager import InterfaceEventManager


class EventDictionary(TypedDict):
    """
    Class for prescribing the structure of event-subscriber-dictionary.
    """
    # name of the event that shall be subscribed to
    event: str
    # list of subscribers subscribing a specified event
    subscribers: list


class EventManager(InterfaceEventManager):
    """
    Class that is handling events.
    """

    # format of subscribers-list: {event:[subscribers]}
    __subscribedEvents: EventDictionary = {}
    __eventProgramExit = ['all', 'exit']

    def subscribeToEvent(self, subscriber: Event, eventName: str) -> None:
        """
        Method for registering a process to the Event-Manager.
        :param subscriber: Object of the class that going to be subscribed.
        :param eventName: Name of the event that is going to be subscribed to.
        """
        # checks if eventName is already in dict and returns it,
        # else sets it as key and empty list as value
        subscribedEventList = self.__subscribedEvents.setdefault(eventName, [])
        if subscriber not in subscribedEventList:
            subscribedEventList.append(subscriber)

    def __notifySubscribers(self, eventName: str, data: any) -> None:
        """
        Notifying the registered processes of the specified event.
        :param eventName: Name of the event posting an update.
        :param data: Data that shall be passed to the receiveEventUpdate-method of subscribed event(s).
        """
        subscribedCallbacksList = self.__subscribedEvents.get(eventName)
        for subscriber in subscribedCallbacksList:
            subscriber.receiveEventUpdate(data)

    def postEventUpdate(self, eventName: str, data: any) -> None:
        """
        Posting event-update to any subscribers listed.
        :param eventName: Name of the event that is posting the update.
        :param data: Data that shall be passed to the subscribers.
        """
        if eventName not in self.__subscribedEvents:
            return
        self.__notifySubscribers(eventName, data)

    def unsubscribeFromEvent(self, subscriber: Event, eventName: str) -> None:
        """
        Method for unsubscribing a class from the Event-Manager.
        :param subscriber: Object of the class that going to be unsubscribed.
        :param eventName: Name of the event that is going to be unsubscribed from.
        """
        if eventName not in self.__subscribedEvents:
            return
        listOfSubscribers = self.__subscribedEvents.get(eventName)
        if subscriber in listOfSubscribers:
            listOfSubscribers.remove(subscriber)
        if len(listOfSubscribers) == 0:
            self.__subscribedEvents.pop(eventName)