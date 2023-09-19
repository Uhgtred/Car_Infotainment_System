#!/usr/bin/env python3
# @author      Markus Kösters
from abc import ABC, abstractmethod


class LoggingInterface(ABC):

    @abstractmethod
    def createLogEntry(self, logLevel: str, moduleName: __name__, message: str) -> None:
        """
        Interface for using the createLogEntry
        :param logLevel: Log-level, that the message shall be stored with.
                        available: 'debug', 'info', 'warning', 'error', 'critical', 'exception'
        :param moduleName: __name__ of the module that has been calling the log-functionality.
        :param message: Log-message that shall be stored.
        """
        ...
