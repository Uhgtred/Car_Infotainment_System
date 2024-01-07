from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from BusTransactions import BusInterfaceFactory


class GetUdpSocketInstance(APIView):
    def get(self, request) -> object:
        socketInstance = BusInterfaceFactory.produceUDP_Transceiver()
        return socketInstance

