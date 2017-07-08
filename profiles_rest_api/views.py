from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPIView(APIView):
    """
    Test APIView
    """

    def get(self, request, format=None):
        """
        Returns a list of APIView features
        """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Its similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Its manually mapped to URLs'
        ]

        return Response({
            'message': 'Hello world',
            'an_apiview': an_apiview
        }
        )
