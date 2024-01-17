#!/usr/bin/env python3
# @author: Markus Kösters

import subprocess
from flask import Response, jsonify
from flask_restful import Resource


class StopServer(Resource):
    """
    Class to create a direct socket-connection to the server.
    """

    def get(self) -> Response:
        """
        Method for shutting down the flask server.
        :return: A response.
        """
        subprocess.run("shutdown -h 0", shell=True, check=True)
        return jsonify("Shutting down!")

