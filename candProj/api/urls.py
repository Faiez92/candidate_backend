from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from candProj.api import views
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', ObtainAuthToken.as_view())
]