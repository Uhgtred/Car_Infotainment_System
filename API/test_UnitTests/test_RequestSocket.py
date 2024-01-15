#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from API import RequestSocket


class test_RequestSocket(unittest.TestCase):

    socketRequest = RequestSocket()

    def test_get(self):
        sock = self.socketRequest.get()
        self.assertListEqual(sock, ['127.0.0.1', 2001])

if __name__ == '__main__':
    unittest.main()
