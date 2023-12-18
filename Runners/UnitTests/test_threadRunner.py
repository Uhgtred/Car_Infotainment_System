#!/usr/bin/env python3
# @author: Markus Kösters
import time
import unittest

from Runners import Threads


def testTask(*args):
    print('Runner Started')
    print(args)
    time.sleep(5)
    print('Runner Stopped')


class MyTestCase(unittest.TestCase):
    testRunner = Threads()

    def test_threadOpening(self):
        self.testRunner.runTask(testTask, ['test', 'test2'])
        assert 'testTask_thread' in self.testRunner._Threads__threads

    def test_threadClosing(self):
        """
        TODO: implement this test
        :return:
        """



if __name__ == '__main__':
    unittest.main()
