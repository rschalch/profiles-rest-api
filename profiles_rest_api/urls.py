from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from profiles_rest_api.views import (
    HelloAPIView,
    HelloViewSet,
    UserProfileViewSet,
    LoginViewSet)


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, base_name='login')


urlpatterns = [
    url(r'hello/', HelloAPIView.as_view()),
    url(r'', include(router.urls))
]
