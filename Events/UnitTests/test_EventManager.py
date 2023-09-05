import unittest

from Events.Event import Event
from Events.EventManager import EventManager


class MyEvent(Event):
    name = 'mytest'
    subscribeTo = 'test'

    def setupEvent(self):
        print('Event successfully set up!')

    def receiveEventUpdate(self, data):
        return f'Data received from Event-Manager: {data}!'

    def postEventUpdate(self, data):
        EventManager().postEventUpdate('test', data)

class MyTestCase(unittest.TestCase):

    eventManager = EventManager()
    event = MyEvent()

    def test_canSubscribeEvent(self):
        print(self.eventManager.subscribeToEvent(self.event, self.event.subscribeTo))
        assert 'test' in self.eventManager._EventManager__subscribedEvents



if __name__ == '__main__':
    unittest.main()
