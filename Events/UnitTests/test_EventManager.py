import unittest

from Events.EventManager import EventManager


class MyEvent:
    name = 'mytest'
    subscribeTo = 'test'

    def setupEvent(self) -> None:
        print('Event successfully set up!')

    def receiveEventUpdate(self, data: any) -> None:
        assert data == 'test'

    def postEventUpdate(self, data: any) -> None:
        EventManager().postEventUpdate('test', data)

class MyTestCase(unittest.TestCase):

    eventManager = EventManager()
    event = MyEvent()

    def test_canSubscribeEvent(self):
        """
        Testing if a specified event can be subscribed to.
        """
        self.eventManager.subscribeToEvent(self.event, self.event.subscribeTo)
        assert ('test' in self.eventManager._EventManager__subscribedEvents
                and self.eventManager._EventManager__subscribedEvents.get('test')[0] == self.event)

    def test_canUnSubscribeEvent(self):
        """
        Testing if a specified event can be unSubscribed from.
        """
        state = False
        self.eventManager.subscribeToEvent(self.event, self.event.subscribeTo)
        if ('test' in self.eventManager._EventManager__subscribedEvents
                and self.eventManager._EventManager__subscribedEvents.get('test')[0] == self.event):
            state = True
        self.eventManager.unsubscribeFromEvent(self.event, self.event.subscribeTo)
        assert (self.eventManager._EventManager__subscribedEvents == {} and state)

    def test_canPostEventUpdate(self):
        """
        Testing if event-update can be posted. Assertion is in MyEvent.receiveEventUpdate.
        """
        self.eventManager.subscribeToEvent(self.event, self.event.subscribeTo)
        self.event.postEventUpdate('test')

    def test_canNotSubscribeToSomething(self):
        """
        Testing if a wrong event can not be subscribed to.
        """
        self.eventManager.subscribeToEvent(self.event, 'Something')
        assert ('test' not in self.eventManager._EventManager__subscribedEvents
                and not self.eventManager._EventManager__subscribedEvents.get('test'))

    def test_canNotUnSubscribeFromSomething(self):
        """
        Testing if a specified event can be unSubscribed from.
        """
        state = False
        self.eventManager.subscribeToEvent(self.event, self.event.subscribeTo)
        if ('test' in self.eventManager._EventManager__subscribedEvents
                and self.eventManager._EventManager__subscribedEvents.get('test')[0] == self.event):
            state = True
        self.eventManager.unsubscribeFromEvent(self.event, 'Something')
        assert (self.eventManager._EventManager__subscribedEvents != {} and state)

    def test_canNotUnSubscribeSomethingFromEvent(self):
        """
        Testing if a specified event can be unSubscribed from.
        """
        state = False
        self.eventManager.subscribeToEvent(self.event, self.event.subscribeTo)
        if ('test' in self.eventManager._EventManager__subscribedEvents
                and self.eventManager._EventManager__subscribedEvents.get('test')[0] == self.event):
            state = True
        self.eventManager.unsubscribeFromEvent('Something', self.event.subscribeTo)
        assert (self.eventManager._EventManager__subscribedEvents != {} and state)

if __name__ == '__main__':
    unittest.main()
