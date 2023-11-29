#!/usr/bin/env python3
# @author Markus Kösters

from BusTransactions import BusFactory
from Events.EventInterface import EventInterface


class Main:
    """
    Main-program. Starts and organizes any submodules
    """

    @staticmethod
    def connectEvents() -> None:
        """
        Method for starting all events listed in the dictionary.
        """
        serialBusTransceiver = BusFactory.produceSerialTransceiver()
        EventInterface.subscribeToEvent(eventName='SerialBusEvent', callbackMethod=serialBusTransceiver.writeSingleMessage)


if __name__ == '__main__':
    main = Main()
    main.connectEvents()
