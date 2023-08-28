#!/usr/bin/env python3
# @author      Markus Kösters
import asyncio
import multiprocessing


class EventReceiver:
    __exit = True

    def startEventReceiver(self, eventPipe: multiprocessing.Pipe, moduleMainMethod: any) -> None:
        """
        Method for starting an event-receiver and a module main-program as well
        """
        # this is the method, that shall start the wished module in a separate process
        moduleMainMethod()
        # starting the event-receiver
        asyncio.run(self.waitForEventStatus(eventPipe))

    async def waitForEventStatus(self, eventPipe: multiprocessing.Pipe):
        """
        Method that is waiting for any event-update to trigger some functionality
        :param eventPipe: <tuple> (callbackMethod: any, argument: any)
        """
        while not self.__exit:
            eventMethod, data = await eventPipe.recv()
            eventMethod(data)
        self.closeSideProcess()

    def closeSideProcess(self):
        pass
