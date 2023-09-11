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
