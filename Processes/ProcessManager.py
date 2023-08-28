#!/usr/bin/env python3
# @author      Markus Kösters
import multiprocessing

from Events import EventReceiver


class ProcessManager:

    __exit = False
    __runningProcesses = []

    def __init__(self):
        self.eventReceiver = EventReceiver()

    def openSubprocess(self, moduleMainMethod: any) -> multiprocessing.Pipe:
        """
        Method for opening a subprocess
        :param moduleMainMethod: Method that shall be executed in new process
        :return: parentPipe, childPipe which can communicate to the process (parentPipe.send(something)/something=parentPipe.recv())
        """
        parentPipe, childPipe = multiprocessing.Pipe()
        process = multiprocessing.Process(target=self.eventReceiver.startEventReceiver, args=(moduleMainMethod, childPipe))
        process.start()
        self.__runningProcesses.append(process)
        return parentPipe, childPipe

    @property
    def exit(self) -> bool:
        return self.exit

    @exit.setter
    def exit(self, exitFlag: bool) -> None:
        self.__exit = exitFlag