#!/usr/bin/env python3
# @author      Markus Kösters

import Event
import EventUser


class ProduceEventUser(EventUser.EventUser):

    def __init__(self):
        """
        Setting up an event-user.
        """
        self.__event = Event.Event()

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


if __name__ == '__main__':
    eventUser = ProduceEventUser()
    eventUser.subscribeToEvent(print)
    eventUser.postEventUpdate('Test')
