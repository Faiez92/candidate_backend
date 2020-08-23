from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from candProj.candidate import views

router = routers.DefaultRouter()
router.register(r'candidates', views.CandidatViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api/', include('candProj.api.urls')),
]
