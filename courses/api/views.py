# system level import
# import os

# framework level libraries
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

# project level imports

# app level imports
from courses.models import Language, Domain, SoftSkills, SoftSkillsData, KnowledgeBase, \
    RandomData

# api level imports
from courses.api.serializers import LanguageSerializer, DomainSerializer, SoftSkillsSerializer, \
    SoftSkillsDataSerializer, KnowledgeBaseSerializer, RandomDataSerializer
from courses.api.pagination import ResourcesPagination


class ReadOnlyCoursesAbstractViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = None
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_fields = []
    ordering_fields = []
    ordering = []
    queryset = None
    pagination_class = ResourcesPagination

    class Meta:
        abstract = True


class LanguageViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for LanguageSerializer
    """
    serializer_class = LanguageSerializer
    filter_fields = ['id', 'language_name', 'slug', 'description']
    ordering_fields = ['language_name']
    ordering = ['language_name']
    queryset = Language.objects.all()


class DomainViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for DomainSerializer
    """
    serializer_class = DomainSerializer
    filter_fields = ['id', 'domain_name', 'slug', 'description']
    ordering_fields = ['domain_name']
    ordering = ['domain_name']
    queryset = Domain.objects.all()


class SoftSkillsViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for SoftSkillsSerializer
    """
    serializer_class = SoftSkillsSerializer
    filter_fields = ['id', 'soft_skill_category', 'slug', 'description']
    ordering_fields = ['soft_skill_category']
    ordering = ['soft_skill_category']
    queryset = SoftSkills.objects.all()


class SoftSkillsDataViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for SoftSkillsDataSerializer
    """
    serializer_class = SoftSkillsDataSerializer
    filter_fields = ['title', 'description', 'slug', 'data_type', 'paid', 'soft_skill']
    ordering_fields = ['data_type', 'title', 'paid']
    ordering = ['data_type']
    queryset = SoftSkillsData.objects.all()

    def get_queryset(self):
        queryset = SoftSkillsData.objects.filter(is_active=True)
        return queryset


class KnowledgeBaseViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for KnowledgeBaseSerializer
    """
    serializer_class = KnowledgeBaseSerializer
    filter_fields = ['title', 'description', 'slug', 'skill_level', 'data_type', 'paid', 'languages', 'domains',
                        'project']
    ordering_fields = ['skill_level', 'data_type', 'title', 'paid']
    ordering = ['skill_level', 'data_type']
    queryset = KnowledgeBase.objects.all()

    def get_queryset(self):
        queryset = KnowledgeBase.objects.filter(is_active=True)
        return queryset


class RandomDataViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for RandomDataSerializer
    """
    serializer_class = RandomDataSerializer
    filter_fields = ['title', 'description', 'slug', 'data_type', 'paid']
    ordering_fields = ['data_type', 'title', 'paid']
    ordering = ['data_type']
    queryset = RandomData.objects.all()

    def get_queryset(self):
        queryset = RandomData.objects.filter(is_active=True)
        return queryset
