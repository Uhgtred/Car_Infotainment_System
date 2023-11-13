#!/usr/bin/env python3
# @author      Markus Kösters

from .Event import Event


class EventFactory:
    """
    Factory-class for EventUser.
    """

    @staticmethod
    def produceEvent():
        return Event()
