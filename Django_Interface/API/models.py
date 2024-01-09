from django.db import models


class SocketModel(models.Model):
    """
    Class for modeling the input parameters for a socket-request.
    """
    port = models.IntegerField()
    socketType = models.CharField(max_length=3)

    def __str__(self):
        # returning socket-Type and port as object information
        return f'{self.socketType}: {self.port}'
