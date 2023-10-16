#!/usr/bin/env python3
# @author: Markus Kösters

import EventUser


# class Event(Protocol):
#     """
#     Protocol to prescribe the structure of an Event.
#     """
#
#     def subscribe(self, callbackMethod: EventUser) -> None:
#         """
#         Subscribe to an event and get a message as soon as there is an update.
#         :param callbackMethod: Method that shall be called on event-update.
#                                 Needs to accept exact one parameter containing message from event <any>.
#         """
#         pass
#
#     def notifySubscribers(self, data: any) -> None:
#         """
#         Notifying subscribers of the Event of any updates.
#         :param data: Message that is to be passed to the subscribers.
#         """
#         pass


# class CanTransmitterEvent:
#     """
#     CAN-Transmitter Event for updating messages that shall be sent to CAN-Bus.
#     """
#
#     __subscribers: list = []
#
#     def subscribe(self, callbackMethod: EventUser) -> None:
#         """
#         Subscribing to Can Transmitter
#         :param callbackMethod: method that the event-update is going to be sent to.
#         """
#         if callbackMethod not in self.__subscribers:
#             self.__subscribers.append(callbackMethod)
#
#     def notifySubscribers(self, data: any) -> None:
#         """
#         Sending an Event-update to all subscribers.
#         """
#         for sub in self.__subscribers:
#             sub.postEventUpdate(data)


class Event:
    """
    Class that represents an event which can be subscribed to and posted to.
    """

    def __init__(self):
        self.__subscribers: list = []

    def subscribe(self, callbackMethod: EventUser.EventUser) -> None:
        """
        Subscribing to Event, receiving any updates occurring.
        :param callbackMethod: Method that the event-update is going to be sent to.
        """
        if callbackMethod not in self.__subscribers:
            self.__subscribers.append(callbackMethod)

    def notifySubscribers(self, data: any) -> None:
        """
        Sending an Event-update to all subscribers.
        :param data: Message-data that shall be sent to subscribers.
        """
        for sub in self.__subscribers:
            sub.postEventUpdate(data)
