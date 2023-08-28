#!/usr/bin/env python3
# @author: Markus Kösters
import multiprocessing

from Processes import ProcessManager, InterfaceEventProcess
from .InterfaceEventManager import InterfaceEventManager


class EventManager(InterfaceEventManager):
    """
    Class that is handling events from processes that are registered
    """

    __registeredProcesses = {str: list(tuple)}
    __eventProgramExit = ['all', 'exit']

    def __init__(self):
        self.processManager = ProcessManager()

    def registerProcess(self, eventProcess: InterfaceEventProcess) -> None:
        """
        Method for registering processes to a specified event
        :param eventProcess: object containing multiple information about the process to be registered
        object can be created using InterfaceEventProcess (see ExampleEventProcess for example).
        """
        if eventProcess.event not in self.__registeredProcesses:
            self.__registeredProcesses[eventProcess.event] = []
        if eventProcess.callbackMethod not in self.__registeredProcesses[eventProcess.event]:
            self.__registeredProcesses[eventProcess.event].append(eventProcess)

    def __notifySubscribers(self, event: str, message: any) -> None:
        """
        Notifying the registered processes of the specified event
        :param event: name of the event used for identification
        :param message: data that shall be passed to the callback-method of the registered process
        """
        for eventID in self.__registeredProcesses:
            if eventID != event and event != 'all':
                continue
            for eventProcess in self.__registeredProcesses[eventID]:
                # sending the method that is to be executed and the message provided to that method
                eventProcess.parentPipe.send(eventProcess.callbackMethod, message)
