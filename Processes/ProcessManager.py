#!/usr/bin/env python3
# @author      Markus Kösters
import multiprocessing

from Events import EventReceiver


class ProcessManager:

    __exit = False
    __runningProcesses = []

    def __init__(self):
        self.eventReceiver = EventReceiver()

    def openSubprocess(self, moduleMainMethod, childPipe: multiprocessing.Pipe) -> None:
        """
        TODO: some description
        """
        process = multiprocessing.Process(target=self.eventReceiver.startEventReceiver, args=(moduleMainMethod, childPipe))
        process.start()
        self.__runningProcesses.append(process)

    @property
    def exit(self) -> bool:
        return self.exit

    @exit.setter
    def exit(self, exitFlag: bool) -> None:
        self.__exit = exitFlag