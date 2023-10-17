#!/usr/bin/env python3
# @author Markus Kösters

import unittest

from Events import ProduceEventUser


class MyTestCase(unittest.TestCase):

    factory = ProduceEventUser()
    testData = 'Test'
    receivedData = None

    def test_subscribeToEvent(self):
        self.factory.subscribeToEvent(self.postEventUpdateHelper)
        assert 'postEventUpdateHelper' in str(self.factory._ProduceEventUser__event._Event__subscribers)

    def test_postEventUpdate(self):
        self.factory.subscribeToEvent(self.postEventUpdateHelper)
        # print(self.factory._ProduceEventUser__event._Event__subscribers)
        self.factory.postEventUpdate(self.testData)
        assert self.receivedData == self.testData

    def postEventUpdateHelper(self, data):
        self.receivedData = data


if __name__ == '__main__':
    unittest.main()
