from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from profiles_rest_api import models
from profiles_rest_api.models import ProfileFeedItem


class HelloSerializer(Serializer):
    """
    Serializes a name field for testing the APIView
    """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(ModelSerializer):
    """
    Serializer for UserProfile objects
    """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and return a user
        """
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(ModelSerializer):

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status', 'created_at',)
        extra_kwargs = {
            'user_profile' : {'read_only': True}
        }
