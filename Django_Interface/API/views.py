from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import SocketSerializer

from BusTransactions import BusInterfaceFactory


class GetSocketInstance(APIView):

    @staticmethod
    def get(request) -> object:
        """
        Getter method for a socket instance to communicate with the server.
        :param request: Information needed: port (int), socket-type ('udp' or 'tcp')
        :return: Socket instance to run ethernet-communication through.
        """
        serializer = SocketSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.socketType == 'udp':
                socketInstance = BusInterfaceFactory.produceUDP_Transceiver(serializer.port)
                return Response(socketInstance, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
