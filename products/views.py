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
    Diagram, 
)

from .serializers import (
    DiagramSerializer, 
)

from .tasks import (
    generate_diagram
)


class DiagramViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Diagram.objects.all()
    serializer_class = DiagramSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        permission_classes = [AllowAny] 
        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        user = self.request.user
        queryset = Diagram.objects.all()
        return queryset  

    @action(methods=['POST'], detail=False)
    def generate_uml(self, request, *args, **kwargs):        

        s = request.body
        u = str(s, 'utf-8')

        #svg_link = generate_diagram(request.body)
        svg_link = generate_diagram(u)
        """
        for item in data:
            item['svg_link'] = generate_diagram(item['chart_text'])
            item['png_link'] = generate_diagram(item['chart_text'], 'png')
        """
        return JsonResponse({'svg_link':svg_link})         

    @action(methods=['POST'], detail=False)
    def create_product(self, request, *args, **kwargs):
        items = []

        html_string = render_to_string('template_profile.html', {'items': items})
        html = HTML(string=html_string)
        pdf_file = html.write_pdf()
        
        file_path = "ssm/product/" + datetime.datetime.utcnow().strftime("%s") + "-" + uuid.uuid4().hex + '.pdf'
        # "mbpj-ghg/application-report/" <-- naming system
        saved_file = default_storage.save(
            file_path, 
            ContentFile(pdf_file)
        )
        
        full_url_path = settings.MEDIA_ROOT + saved_file
        # print(full_url_path)

        serializer = 'https://pipeline-project.sgp1.digitaloceanspaces.com/'+full_url_path
        return Response(serializer)