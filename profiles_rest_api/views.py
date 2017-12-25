from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from profiles_rest_api.models import UserProfile
from profiles_rest_api.permissions import UpdateOwnProfile
from profiles_rest_api.serializers import (
    HelloSerializer,
    UserProfileSerializer
)

class HelloAPIView(APIView):
    """
    Test APIView
    """
    serializer_class = HelloSerializer

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

    def post(self, request):
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'delete'})


class HelloViewSet(ViewSet):

    serializer_class = HelloSerializer

    def list(self, request):

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically routes to urls using routers',
            'Provide more functionality with less code',
            'Recommended for standard CRUD operations',
            'Not so customizable like the APIView',
        ]

        response = {
            'message': 'hello viewset!',
            'a_viewset': a_viewset,
        }

        return Response(response)

    def create(self, request):

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)

            return Response({'message': message})

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(ModelViewSet):
    """
    Handles creating, reading and updating profiles
    """

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(ViewSet):
    """Checks email, password and returns an AuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)

