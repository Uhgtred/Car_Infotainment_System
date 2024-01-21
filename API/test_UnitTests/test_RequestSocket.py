#!/usr/bin/env python3
# @author: Markus Kösters
import json
import time
import unittest
import requests

from API import RequestSocket, Main


class test_RequestSocket(unittest.TestCase):
    socketRequest = RequestSocket()
    mainObject = None

    def setUp(self):
        self.mainObject = Main()
        self.mainObject.main()
        time.sleep(5)

    def test_get(self):
        sock = requests.get('http://127.0.0.1:2000/getSocketAddress')
        sockResponse = json.loads(sock.content)
        self.assertListEqual(sockResponse, ['127.0.0.1', 2001])
        # print(requests.get('http://127.0.0.1:2000/shutdown').content)


if __name__ == '__main__':
    unittest.main()
