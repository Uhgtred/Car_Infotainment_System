#!/usr/bin/env python3
# @author      Markus Kösters

import multiprocessing
from abc import ABC, abstractmethod
from dataclasses import dataclass

from .ProcessManager import ProcessManager


@dataclass
class InterfaceEventProcess(ABC):
    __processManager = ProcessManager
    event: str
    callbackMethod: any
    parentPipe: multiprocessing.Pipe
    __exit: bool = False

    @abstractmethod
    def startEventProcess(self, moduleMainMethod: callable) -> multiprocessing.Pipe:
        """
        Method for starting an event-receiver and a module main-program as well
        """
        ...

    @abstractmethod
    async def waitForEventStatus(self) -> None:
        """
        Method that is waiting for any event-update to trigger some functionality
        """
        ...

    @abstractmethod
    def closeEventProcess(self):
        """
        Method used to close the running event-process
        """
        ...
