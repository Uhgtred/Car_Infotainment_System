#!/usr/bin/env python3
# @author Markus Kösters

import unittest

from Events import EventManager, Event
from Events.EventFactory import EventObjectFactory, EventFactory


class MyTestCase(unittest.TestCase):

    def test_canCreateEventObject(self):
        name = 'testEvent'
        module = TestEvent
        subscribeTo = 'testPoster'
        objectFactory = EventObjectFactory(module, name, subscribeTo)
        assert str(type(objectFactory)) == "<class 'Events.EventFactory.EventObjectFactory'>"

    def test_canSetupEvent(self):
        name = 'testEvent'
        module = TestEvent
        subscribeTo = 'testPoster'
        eventFactory = EventFactory()
        eventFactory.setupEvent(module, name, subscribeTo)
        self.postEventUpdateHelper()

    def postEventUpdateHelper(self):
        EventManager().postEventUpdate('testPoster', 'Hello World')


class TestEvent:
    def __init__(self):
        self.eventManager = EventManager()

    def sendMessage(self, callbackMethod: Event.sendMessage, loop: bool = True) -> None:
        """
        Method that receives messages from an Event (optionally only one message).
        :param callbackMethod: Method that the read message shall be passed to.
        :param loop: True: reading messages constantly, False: reading only one message.
        """
        callbackMethod('testPoster', 'Hello World')

    def receiveMessage(self, data: any) -> None:
        """
        Method that sends messages to an Event-subscriber.
        :param data: message that shall be sent to subscriber
        """
        assert data == 'Hello World'


if __name__ == '__main__':
    unittest.main()
