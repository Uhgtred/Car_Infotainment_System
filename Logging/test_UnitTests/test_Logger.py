#!/usr/bin/env python3
# @author      Markus Kösters
import os
import time
import unittest

from Logging.Logger import Logger


class MyTestCase(unittest.TestCase):
    logger = Logger()
    basePath = os.path.dirname(__file__)
    logfile = os.path.join(basePath, 'test_Logger.log')

    def test_createLogEntry(self):
        testDict = {'1stTest': 'info', '2ndTest': 'info', '3rdTest': 'warning'}
        for key in testDict:
            self.logger.createLogEntry(testDict.get(key), __name__, key)
        if not os.path.exists(self.logfile):
            with open(self.logfile, 'w') as logFile:
                pass
        with open(self.logfile, 'r') as logFile:
            lines = logFile.readlines()
        for line in lines:
            assert 'Test' in line


if __name__ == '__main__':
    unittest.main()
