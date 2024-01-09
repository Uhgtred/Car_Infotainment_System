#!/usr/bin/env python3
# @author: Markus Kösters

from rest_framework import serializers


class SocketSerializer(serializers.ModelSerializer):
    """
    Method for serializing data needed to create a socket object.
    """
    port = serializers.IntegerField()
    socketType = serializers.CharField()
