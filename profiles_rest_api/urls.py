from django.conf.urls import url

from profiles_rest_api.views import HelloAPIView

urlpatterns = [
    url(r'hello/', HelloAPIView.as_view())
]
