from rest_framework import viewsets
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
)

from feedback.api.serializers import FeedbackSerializer
from .permissions import IsOwner
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from courses.api.pagination import ResourcesPagination


class FeedbackViewSet(viewsets.ModelViewSet):
	serializer_class = FeedbackSerializer
	pagination_class = ResourcesPagination

