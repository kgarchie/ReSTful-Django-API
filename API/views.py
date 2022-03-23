from django.shortcuts import render
from .models import News
from .serializers import NewsSerializer
# from rest_framework import permissions
from rest_framework import viewsets


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('date_time')
    serializer_class = NewsSerializer

    # permission_classes = [permissions.IsAuthenticated]
