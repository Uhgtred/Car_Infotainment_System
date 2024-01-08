#!/usr/bin/env python3
# @author: Markus Kösters

from rest_framework import serializers
from API import models


class SocketSerializer(serializers.ModelSerializer):
    """
    Method for serializing data needed to create a socket object.
    """
    port = serializers.IntegerField()
    socketType = serializers.CharField()
