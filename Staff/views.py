from django.shortcuts import render
from rest_framework import viewsets
from .models import Workers, Jobs, Company
from .serializers import WorkersSerializer, JobsSerializer, CompanySerializer


# Create your views here.


class WorkersViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all().order_by('-id')
    serializer_class = WorkersSerializer
    lookup_field = "id"


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    lookup_field = "id"


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "id"
