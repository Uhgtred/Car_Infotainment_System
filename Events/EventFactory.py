#!/usr/bin/env python3
# @author      Markus Kösters

from dataclasses import dataclass

from .EventManager import EventManager
from .Event import Event


@dataclass
class EventObjectFactory:
    """
    Factory for creating an object that can be handled by the Eventmanager.
    EVENT-FACTORY IS USING THIS, NO NEED TO USE IT MANUALLY!
    """
    module: callable
    name: str
    subscribeTo: str

    def createEventObject(self) -> object:
        """
        Method creating an object of the passed module and attaching
        the attributes needed by event-module.
        """
        module = self.module()
        module.name = self.name
        module.subscribeTo = self.subscribeTo
        return module


class EventFactory:

    def __init__(self):
        self.manager = EventManager()

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
        instanceObject.sendMessage(callbackMethod, loop=True)