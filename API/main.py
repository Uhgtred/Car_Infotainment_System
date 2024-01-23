#!/usr/bin/env python3
# @author: Markus Kösters

import threading
from flask import Flask
from flask_restful import Api

from API import RequestSocket
from API.StopServer import RestartServer


class Main:
    """
    Main class for setting up and starting the Flask application and API.
    """

    """
    from multiprocessing import Process

    server = Process(target=app.run)
    server.start()
    # ...
    server.terminate()
    server.join()
    """

    __app = Flask(__name__)
    __resources: dict = {
        RequestSocket: '/getSocketAddress',
        RestartServer: '/restartAPIServer'
    }

    def __init__(self):
        self.app = Flask('InfotainmentAPI')
        self.api = Api(self.app)

    def add_routes(self) -> None:
        """
        Method that adds routes to the api instance.
        """
        for resource in self.__resources:
            self.api.add_resource(resource, self.__resources.get(resource))

    @property
    def getResources(self) -> dict:
        """
        Getter-method for the possible requests to th api.
        :return: Dictionary with the methods available for the api and their url.
        """
        return self.__resources

    def main(self) -> None:
        """
        Main method that starts the api server.
        """
        thread = threading.Thread(target=self.runServer)
        thread.start()

    def runServer(self) -> None:
        self.add_routes()
        self.app.run(host='127.0.0.1', port=2000)


if __name__ == '__main__':
    Main().main()
