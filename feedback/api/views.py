from rest_framework import viewsets
from rest_framework.permissions import(
    AllowAny,
)
from feedback.api.serializers import FeedbackSerializer
from feedback.models import Feedback
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)
from .permissions import IsOwnerFeedback
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from courses.api.pagination import ResourcesPagination


class FeedbackViewSet(viewsets.ModelViewSet):
	"""
	handles viewset for feedback serializer.
	"""
	serializer_class = FeedbackSerializer
	pagination_class = ResourcesPagination
	permission_classes = [AllowAny,IsOwnerFeedback]
	filter_backends = [filters.DjangoFilterBackend,SearchFilter, OrderingFilter]
	search_fields = ['id','text']
	ordering = ('-created_at')
	queryset = Feedback.objects.all()

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

	def perform_create(self, serializer):
		if self.request.user.id == None:
		    # Handles anonymous users
		    serializer.save(user=self.request.user.id)
		else:
		    serializer.save(user=self.request.user)

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

	def get_queryset(self):
		user = self.request.user.id
		# Get objects only associated with the requesting user
		queryset = Feedback.objects.filter(user=user)
		return queryset





