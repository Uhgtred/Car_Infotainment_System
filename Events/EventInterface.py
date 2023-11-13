#!/usr/bin/env python3
# @author: Markus Kösters

from Events.EventFactory import EventFactory


class EventInterface:

    __events: dict = {}

    def createNewEvent(self, name: str) -> __events:
        """
        Method for creating a new event.
        :param name: Clear name of the event. Existing events can be received by calling getEventsList.
        :return: List of available Events.
        """
        instance = EventFactory.produceEvent()
        self.__events[name].append(instance)
        return list(self.__events.keys())

    @property
    def getEventsList(self) -> list[str]:
        """
        Getter Method for Events available.
        :return: List of available Events.
        """
        return list(self.__events.keys())

    def subscribeToEvent(self, eventName: str, callbackMethod: callable) -> None:
        """
        Method for subscribing to an existing Event.
        :param eventName: Clear name of the event. Existing events can be received by calling getEventsList.
        :param callbackMethod: Method that is going to be used to call back when event-update occurs.
        """
        if eventName in self.__events:
            self.__events.get(eventName).subscribe(callbackMethod=callbackMethod)

    def postEventUpdate(self, eventName: str, data: any) -> None:
        """
        Method for notifying subscribers of an event.
        :param eventName: Clear name of the event. Existing events can be received by calling getEventsList.
        :param data: Data that will be shared to the subscribers.
        """
        if eventName in self.__events:
            self.__events.get(eventName).notifySubscribers(data=data)
