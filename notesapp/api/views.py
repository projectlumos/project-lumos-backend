from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from courses.api.pagination import ResourcesPagination
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from notesapp.models import KnowledgeBaseNotes, SoftSkillsDataNotes, RandomDataNotes
from notesapp.api.serializers import KnowledgeBaseNotesSerializer, SoftSkillsDataNotesSerializer, \
	RandomDataNotesSerializer
from notesapp.api.permissions import IsOwner

class KnowledgeBaseNotesViewset(ModelViewSet):
	"""
	Handles Views for KnowledgeBaseNotesSerializer
	"""
	serializer_class = KnowledgeBaseNotesSerializer
	permission_classes = [IsAuthenticated,IsOwner]
	pagination_class = ResourcesPagination
	queryset=KnowledgeBaseNotes.objects.all()
	filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
	filter_fields = ['id', 'resource', 'title', 'slug', 'content']
	ordering = ('-created_at')

	def perform_create(self,serializer):
		# Save the notes against the user requesting it.
		serializer.save(user=self.request.user)

	def list(self,request,*args,**kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = KnowledgeBaseNotesSerializer(queryset,many=True,context={'request':request})
		return Response(serializer.data)

	def get_queryset(self):
		user = self.request.user.id
		# Get the notes object of the user requesting it
		queryset_list = KnowledgeBaseNotes.objects.filter(user=user)
		return queryset_list


class SoftSkillsDataNotesViewset(ModelViewSet):
	"""
	Handles Views for SoftSkillsDataNotesSerializer
	"""
	serializer_class = SoftSkillsDataNotesSerializer
	permission_classes = [IsAuthenticated,IsOwner]
	pagination_class = ResourcesPagination
	queryset=SoftSkillsDataNotes.objects.all()
	filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
	filter_fields = ['id', 'resource', 'title', 'slug', 'content']
	ordering = ('-created_at')

	def perform_create(self,serializer):
		# Save the notes against the user requesting it.
		serializer.save(user=self.request.user)

	def list(self,request,*args,**kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = SoftSkillsDataNotesSerializer(queryset,many=True,context={'request':request})
		return Response(serializer.data)

	def get_queryset(self):
		user = self.request.user.id
		# Get the notes object of the user requesting it.
		queryset_list = SoftSkillsDataNotes.objects.filter(user=user)
		return queryset_list


class RandomDataNotesViewset(ModelViewSet):
	"""
	Handles Views for RandomDataNotesSerializer
	"""
	serializer_class = RandomDataNotesSerializer
	permission_classes = [IsAuthenticated,IsOwner]
	pagination_class = ResourcesPagination
	queryset=RandomDataNotes.objects.all()
	filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
	filter_fields = ['id', 'resource', 'title', 'slug', 'content']
	ordering = ('-created_at')

	def perform_create(self,serializer):
		# Save the notes against the user requesting it.
		serializer.save(user=self.request.user)

	def list(self,request,*args,**kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = RandomDataNotesSerializer(queryset,many=True,context={'request':request})
		return Response(serializer.data)

	def get_queryset(self):
		user = self.request.user.id
		# Get the notes object of the user requesting it.
		queryset_list = RandomDataNotes.objects.filter(user=user)
		return queryset_list
