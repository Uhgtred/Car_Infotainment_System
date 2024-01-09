#!/usr/bin/env python3
# @author: Markus Kösters

from django.urls import path
from .views import GetUdpSocketInstance

urlpatterns = [
    path('getUdpSocketInstance', GetUdpSocketInstance, name='getUDPTransceiver')
]
