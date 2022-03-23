from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

app_name = 'API'

urlpatterns = [
    path('API/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]