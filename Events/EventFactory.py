#!/usr/bin/env python3
# @author      Markus Kösters

from .Event import Event
from .EventUser import EventUser


class EventFactory:
    """
    Factory-class for EventUser.
    """

    @staticmethod
    def produceEventUser():
        return ProduceEventUser()


class ProduceEventUser(EventUser):
    """
    Helper-class for the EventFactory to produce an Eventuser.
    """

    def __init__(self):
        """
        Setting up an event-user.
        """
        self.__event = Event()

    def subscribeToEvent(self, eventCallbackMethod: callable) -> None:
        """
        Method for subscribing to event-instance.
        :param eventCallbackMethod: Method that shall be informed about event-updates.
                                    Has to receive one parameter, containing the message of the event-update.
        """
        self.__event.subscribe(eventCallbackMethod)

    def postEventUpdate(self, data: any) -> None:
        """
        Method for posting updates to an event.
        """
        self.__event.notifySubscribers(data)
