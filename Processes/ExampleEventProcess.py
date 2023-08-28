#!/usr/bin/env python3
# @author      Markus Kösters
import asyncio
import multiprocessing

from .InterfaceEventProcess import InterfaceEventProcess


class EventProcess(InterfaceEventProcess):
    exit = True

    def __init__(self):
        self.childPipe = None

    def startEventProcess(self, moduleMainMethod: callable) -> multiprocessing.Pipe:
        """
        Method for starting an event-receiver and a module main-program as well
        """
        # this is the method, that shall start the wished module in a separate process
        parentPipe, self.childPipe = self.__processManager.openSubprocess(self.__run)
        return parentPipe

    def __run(self, moduleMainMethod: any):
        moduleMainMethod()
        # starting the event-receiver
        asyncio.run(self.waitForEventStatus())

    async def waitForEventStatus(self):
        """
        Method that is waiting for any event-update to trigger some functionality
        """
        while not self.exit:
            eventMethod, data = await self.childPipe.recv()
            eventMethod(data)

    def closeEventProcess(self):
        self.exit = True
