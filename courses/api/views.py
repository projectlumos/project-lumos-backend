from rest_framework import viewsets
from .serializers import LanguageSerializer, DomainSerializer, VideoSerializer, ExternalLinkSerializer
from courses.models import Language, Domain, Video, ExternalLink
from .pagination import VideoPageNumberPagination, ExternalLinkPageNumberPagination
from rest_framework.permissions import(
    AllowAny
)
from django_filters import rest_framework as filters
from rest_framework.filters import (
    OrderingFilter
)


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    handles viewset for LanguageSerializer
    """
    serializer_class = LanguageSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_fields = ['id','language_name', 'slug', 'description']
    ordering_fields = ['language_name']
    ordering = ['language_name']
    queryset = Language.objects.all()


class DomainViewSet(viewsets.ReadOnlyModelViewSet):
    """
    handles viewset for DomainSerializer
    """
    serializer_class = DomainSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_fields = ['id','domain_name', 'slug', 'description']
    ordering_fields = ['domain_name']
    ordering = ['domain_name']
    queryset = Domain.objects.all()


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    handles viewset for VideoSerializer
    """
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    pagination_class = VideoPageNumberPagination
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_fields = ['title', 'description', 'slug', 'skill_level', 'languages', 'domains']
    ordering_fields = ['skill_level', 'title']
    ordering = ['skill_level']
    queryset = Video.objects.all()

    def get_queryset(self):
        queryset = Video.objects.filter(is_active=True)
        return queryset


class ExternalLinkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    handles viewset for ExternalLinkSerializer
    """
    serializer_class = ExternalLinkSerializer
    permission_classes = [AllowAny]
    pagination_class = ExternalLinkPageNumberPagination
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_fields = ['title', 'description', 'slug', 'skill_level', 'external_type', 'paid', 'languages', 'domains']
    ordering_fields = ['skill_level', 'external_type', 'title', 'paid']
    ordering = ['skill_level', 'external_type']
    queryset = ExternalLink.objects.all()

    def get_queryset(self):
        queryset = ExternalLink.objects.filter(is_active=True)
        return queryset
