#!/usr/bin/env python3
# @author: Markus Kösters

from rest_framework import serializers
from API.models import pass

class passSerializer(serializers.ModelSerializer):
    class Meta:
        model = pass
        fields = '__all__'