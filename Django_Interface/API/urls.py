#!/usr/bin/env python3
# @author: Markus Kösters

from django.urls import path
from .views import GetSocketInstance

urlpatterns = [
    path('getSocketInstance', GetSocketInstance, name='getUDPTransceiver')
]
