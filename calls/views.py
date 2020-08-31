import datetime
import json
import uuid
import tempfile


from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.files.storage import default_storage
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from core.helpers import PathAndRename

from .models import (
    Call, 
)

from .serializers import (
    CallSerializer, 
)

from .helpers import (
    call_middleware
)


class CallViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        permission_classes = [AllowAny] 
        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        user = self.request.user
        queryset = Call.objects.all()
        return queryset  

    @action(methods=['GET'], detail=False)
    def services(self, request, *args, **kwargs):        

        s = request.body
        u = str(s, 'utf-8')     

        request_service_name = request.GET.get('name', '')
        if request_service_name:
            response_json = call_middleware(1,2)
        else:
            response_json = call_middleware('getBasicCompProf','960536X')         

        return JsonResponse(response_json)         
