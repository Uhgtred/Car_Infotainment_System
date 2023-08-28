#!/usr/bin/env python3
# @author: Markus Kösters
import this
from abc import abstractmethod, ABC
from Processes import InterfaceEventProcess


class InterfaceEventManager(ABC):
    """
    Class for handling Events and notifying subscribers
    """

    @abstractmethod
    def registerProcess(self, eventProcess: InterfaceEventProcess) -> None:
        """
        Method for registering a process to the eventhandler
        """
        ...
