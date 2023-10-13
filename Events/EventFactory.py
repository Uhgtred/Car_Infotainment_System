#!/usr/bin/env python3
# @author      Markus Kösters

from dataclasses import dataclass

<<<<<<< Updated upstream
from .EventManager import EventManager
from .Event import Event
=======
from Microcontrollers.InterfaceTransceiver import Transceiver
from .EventSubscriber import EventSubscriber
from .EventUpdater import EventUpdater
>>>>>>> Stashed changes


class UpdateCanTransmitter:

<<<<<<< Updated upstream
    def createEventObject(self) -> object:
=======
    __subscribers: list = []

    def subscribe(self, module: type(EventSubscriber)) -> None:
>>>>>>> Stashed changes
        """

        :param module: method that the event-update is going to be sent to.
        """
        self.__subscribers.append(module)

    def notifySubscribers(self, data: any) -> None:
        """
        Sending an Event-update to all subscribers.
        """
        for sub in self.__subscribers:
            sub.sendNotification(data)


<<<<<<< Updated upstream
class EventFactory:
=======
class CanTransmitter(EventSubscriber):
>>>>>>> Stashed changes

    def __init__(self):
        self.transceiver = Transceiver('')

<<<<<<< Updated upstream
    def setupEvent(self, module: Event, name: str, subscribeTo: str) -> None:
        """
        Method for configuring the concrete Event.
        :param module: reference of the class that shall be instanced and used as an event.
        :param name: naming for the event, that is being used to subscribe other events to.
        :param subscribeTo: string representing the event that this module shall be subscribed to.
        """
        factory = EventObjectFactory(module, name, subscribeTo)
        instanceObject = factory.createEventObject()
        # enabling Event to send an update to the event-manager
        self.__configurePostEventUpdate(instanceObject)
        # enabling Event to receive an update FROM event-manager
        self.manager.subscribeToEvent(instanceObject, subscribeTo)

    def __configurePostEventUpdate(self, instanceObject: callable) -> None:
        """
        Method for constantly posting updates to the subscribers.
        :param instanceObject: instance-object of the event that is being setup
        """
        callbackMethod = self.manager.postEventUpdate
        instanceObject.receiveMessage(callbackMethod, loop=True)
=======
    def sendNotification(self, data: any) -> None:
        """
        The subscriber is being sent an update.
        """
        self.transceiver.sendMessage(data)


channel = UpdateCanTransmitter()
channel.subscribe(CanTransmitter())
channel.notifySubscribers('Test')
>>>>>>> Stashed changes
