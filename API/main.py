#!/usr/bin/env python3
# @author: Markus Kösters

from flask import Flask
from flask_restful import Api

from API import RequestSocket


class main:

    __resources: dict = {RequestSocket: '/getSocketPort'}

    def __init__(self):
        app = Flask('InfotainmentAPI')
        self.api = Api(app)
        self.add_routes()
        app.run(host='127.0.0.1', port=2000)

    def add_routes(self) -> None:
        """
        Method that adds routes to the api instance.
        """
        for resource in self.__resources:
            self.api.add_resource(resource, self.__resources.get(resource))

    def getResources(self) -> dict:
        """
        Getter-method for the possible requests to th api.
        :return: Dictionary with the methods available for the api and their url.
        """
        return self.__resources


if __name__ == '__main__':
    instance = main()
