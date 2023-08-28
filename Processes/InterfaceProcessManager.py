#!/usr/bin/env python3
# @author      Markus Kösters
import multiprocessing
from abc import ABC, abstractmethod


class InterfaceProcessManager(ABC):

    __exit = False
    __runningProcesses = []

    @abstractmethod
    def openSubprocess(self, moduleMainMethod: any, childPipe: multiprocessing.Pipe) -> None:
        """
        TODO: some description
        """
        ...
