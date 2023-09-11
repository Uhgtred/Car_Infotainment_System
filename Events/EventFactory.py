#!/usr/bin/env python3
# @author      Markus Kösters
from dataclasses import dataclass

from Events import EventManager


@dataclass
class EventObjectFactory:
    """
    Factory for creating an object that can be handled by the Eventmanager.
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

    def setupEvent(self, eventObject: callable, name: str, subscribeTo: str) -> None:
        """
        Method for configuring the concrete Event.
        """
        instanceObject = EventObjectFactory(eventObject, name, subscribeTo)
        manager = EventManager()
        self.__postEventUpdate(instanceObject.module, manager)
        manager.subscribeToEvent(instanceObject.module, subscribeTo)

    @staticmethod
    def __postEventUpdate(module: callable, manager: EventManager) -> None:
        """
        Method for constantly posting can-messages from the arduino
        to the Event-Manager.
        :param module: instance-object of the event that is being setup
        :param manager: instance-object of the eventmanager
        """
        callbackMethod = manager.postEventUpdate
        module.receiveMessage(callbackMethod, loop=True)