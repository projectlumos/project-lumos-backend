from rest_framework import mixins
from rest_framework import viewsets
from .serializers import LanguageSerializer, DomainSerializer, VideoSerializer, ExternalLinkSerializer
from courses.models import Language, Domain, Video, ExternalLink
from .pagination import VideoPageNumberPagination, ExternalLinkPageNumberPagination
from rest_framework.permissions import(
    AllowAny
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)


class LanguageViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    handles viewset for LanguageSerializer
    """
    serializer_class = LanguageSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['language_name', 'slug', 'description']
    ordering_fields = ['language_name']
    ordering = ['language_name']
    queryset = Language.objects.all()


class DomainViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    handles viewset for DomainSerializer
    """
    serializer_class = DomainSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['domain_name', 'slug', 'description']
    ordering_fields = ['domain_name']
    ordering = ['domain_name']
    queryset = Domain.objects.all()


class VideoViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    handles viewset for VideoSerializer
    """
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    pagination_class = VideoPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'slug', 'skill_level']
    ordering_fields = ['skill_level', 'title']
    ordering = ['skill_level']
    queryset = Video.objects.filter(is_active=True)


class ExternalLinkViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    handles viewset for ExternalLinkSerializer
    """
    serializer_class = ExternalLinkSerializer
    permission_classes = [AllowAny]
    pagination_class = ExternalLinkPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'slug', 'skill_level', 'external_type', 'paid']
    ordering_fields = ['skill_level', 'external_type', 'title', 'paid']
    ordering = ['skill_level', 'external_type']
    queryset = ExternalLink.objects.filter(is_active=True)
