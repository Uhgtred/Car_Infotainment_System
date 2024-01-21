#!/usr/bin/env python3
# @author: Markus Kösters

import subprocess
from flask import Response, jsonify
from flask_restful import Resource


class RestartServer(Resource):
    """
    Class to create a direct socket-connection to the server.
    """

    def get(self) -> Response:
        """
        Method for shutting down the flask server.
        :return: A response informing about restarting the server.
        """
        subprocess.run("shutdown -r 0", shell=True, check=True)  # -r restart -h shutdown
        return jsonify("Restarting API-Server!")
