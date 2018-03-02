# system level import
# import os

# framework level libraries
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

# project level imports

# app level imports
from courses.models import Language, Domain, Video, ExternalLink

# api level imports
from courses.api.serializers import LanguageSerializer, DomainSerializer, VideoSerializer, \
    ExternalLinkSerializer
from courses.api.pagination import ResourcesPagination


class ReadOnlyCoursesAbstractViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = None
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_fields = []
    ordering_fields = []
    ordering = []
    queryset = Language.objects.all()
    pagination_class = ResourcesPagination

    class Meta:
        abstract = True


class LanguageViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for LanguageSerializer
    """
    serializer_class = LanguageSerializer
    filter_fields = ['id', 'language_name', 'slug', 'description', 'languages_for']
    ordering_fields = ['language_name']
    ordering = ['language_name']
    queryset = Language.objects.all()


class DomainViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for DomainSerializer
    """
    serializer_class = DomainSerializer
    filter_fields = ['id','domain_name', 'slug', 'description', 'domains_for']
    ordering_fields = ['domain_name']
    ordering = ['domain_name']
    queryset = Domain.objects.all()


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    handles viewset for VideoSerializer
    """
    serializer_class = VideoSerializer
    filter_fields = ['title', 'description', 'slug', 'skill_level', 'languages', 'domains']
    ordering_fields = ['skill_level', 'title']
    ordering = ['skill_level']
    queryset = Video.objects.all()

    def get_queryset(self):
        queryset = Video.objects.filter(is_active=True)
        return queryset


class ExternalLinkViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for ExternalLinkSerializer
    """
    serializer_class = ExternalLinkSerializer
    filter_fields = ['title', 'description', 'slug', 'skill_level', 'external_type', 'paid', 'languages', 'domains']
    ordering_fields = ['skill_level', 'external_type', 'title', 'paid']
    ordering = ['skill_level', 'external_type']
    queryset = ExternalLink.objects.all()

    def get_queryset(self):
        queryset = ExternalLink.objects.filter(is_active=True)
        return queryset
