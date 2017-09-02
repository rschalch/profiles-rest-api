from rest_framework import serializers
from rest_framework.serializers import Serializer


class HelloSerializer(Serializer):
    """
    Serializes a name field for testing the APIView
    """
    name = serializers.CharField(max_length=10)
