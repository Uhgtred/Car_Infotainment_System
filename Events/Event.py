#!/usr/bin/env python3
# @author      Markus Kösters

from typing import Protocol

from Events import EventManager
from Events.EventFactory import EventObjectFactory
from Microcontrollers.Transceiver import CAN_Transceiver


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

    @staticmethod
    def __postEventUpdate(module: callable, manager: EventManager) -> None:
        """
        Method for posting event-updates to the Event-Manager.
        """
        ...


class CAN_TransceiverEvent:

    name: str = 'can_transceiver'
    subscribeTo: str = 'sendCAN_message'

    def setupEvent(self) -> None:
        """
        Method for configuring the concrete Event.
        """
        can_transceiver = EventObjectFactory(CAN_Transceiver, self.name, self.subscribeTo)
        manager = EventManager()
        self.__postEventUpdate(can_transceiver.module, manager)
        manager.subscribeToEvent(can_transceiver.module, self.subscribeTo)

    @staticmethod
    def __postEventUpdate(module: callable, manager: EventManager) -> None:
        """
        Method for constantly posting can-messages from the arduino
        to the Event-Manager.
        """
        callbackMethod = manager.postEventUpdate
        module.receiveMessage(callbackMethod, loop=True)
