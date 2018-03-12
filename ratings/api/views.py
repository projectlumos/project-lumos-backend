# system level import
# import os

# framework level libraries
from rest_framework import viewsets
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
)
from .permissions import IsOwner
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status

# project level imports

# app level imports
from ratings.models import KnowledgeBaseRating, SoftSkillsDataRating, RandomDataRating

# api level imports
from ratings.api.serializers import KnowledgeBaseRatingSerializer, SoftSkillsDataRatingSerializer, \
    RandomDataRatingSerializer

from courses.api.pagination import ResourcesPagination

class RatingsAbstractViewSet(viewsets.ModelViewSet):
    """
    Base viewset
    """
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


class KnowledgeBaseRatingViewSet(RatingsAbstractViewSet):
    """
    handles viewset for KnowledgeBaseRating
    """
    serializer_class = KnowledgeBaseRatingSerializer
    pagination_class = ResourcesPagination
    permission_classes = [IsOwner]
    filter_fields = ['id', 'resource']
    ordering_fields = ['id', 'resource']
    ordering = ['id']
    queryset = KnowledgeBaseRating.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        if self.request.user.id == None:
            serializer.save(user=self.request.user.id)
        else:
            serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user.id
        # get objects only associated with the requesting user
        queryset = KnowledgeBaseRating.objects.filter(user=user)
        return queryset


class SoftSkillsDataRatingViewSet(RatingsAbstractViewSet):
    """
    handles viewset for SoftSkillsDataRatingViewSet
    """
    serializer_class = SoftSkillsDataRatingSerializer
    pagination_class = ResourcesPagination
    permission_classes = [IsOwner]
    filter_fields = ['id', 'resource']
    ordering_fields = ['id', 'resource']
    ordering = ['id']
    queryset = SoftSkillsDataRating.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        if self.request.user.id == None:
            serializer.save(user=self.request.user.id)
        else:
            serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user.id
        # get objects only associated with the requesting user
        queryset = SoftSkillsDataRating.objects.filter(user=user)
        return queryset


class RandomDataRatingViewSet(RatingsAbstractViewSet):
    """
    handles viewset for RandomDataRatingViewSet
    """
    serializer_class = RandomDataRatingSerializer
    pagination_class = ResourcesPagination
    permission_classes = [IsOwner]
    filter_fields = ['id', 'resource']
    ordering_fields = ['id', 'resource']
    ordering = ['id']
    queryset = RandomDataRating.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        if self.request.user.id == None:
            serializer.save(user=self.request.user.id)
        else:
            serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user.id
        # get objects only associated with the requesting user
        queryset = RandomDataRating.objects.filter(user=user)
        return queryset
