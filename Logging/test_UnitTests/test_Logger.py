#!/usr/bin/env python3
# @author      Markus Kösters
import os
import time
import unittest

from Logging.Logger import Logger


class MyTestCase(unittest.TestCase):
    logger = Logger()
    basePath = os.path.dirname(__file__)

    def test_createLogEntry(self):
        testDict = {'1stTest': 'info', '2ndTest': 'info', '3rdTest': 'warning'}
        for key in testDict:
            self.logger.createLogEntry(testDict.get(key), __name__, key)
        with open(os.path.join(self.basePath, 'test_Logger.log'), 'r') as logFile:
            lines = logFile.readlines()
        for line in lines:
            assert 'Test' in line


if __name__ == '__main__':
    unittest.main()
