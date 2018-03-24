# framework level libraries
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
    )
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# app level imports
from notesapp.models import KnowledgeBaseNotes, SoftSkillsDataNotes, RandomDataNotes

# api level imports
from courses.api.pagination import ResourcesPagination
from notesapp.api.serializers import KnowledgeBaseNotesSerializer, SoftSkillsDataNotesSerializer, \
	RandomDataNotesSerializer
from notesapp.api.permissions import IsOwnerNotes


class KnowledgeBaseNotesViewset(ModelViewSet):
	"""
	Handles Views for KnowledgeBaseNotesSerializer
	request : http://127.0.0.1:8000/api/knowledge-base-notes/
    response :
    {
    "count": 1,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/knowledge-base-notes/",
    "results": [
            {
                "url": "http://127.0.0.1:8000/api/knowledge-base-notes/1/",
    			"id": 1,
    			"user": 1,
    			"resource": 9,
    			"title": "New",
    			"content": "new",
    			"slug": "new",
    			"created_at": "2018-03-15T09:45:10.474941Z",
    			"modified_at": "2018-03-15T09:46:54.265141Z"
            }
        ]
    }
	"""
	serializer_class = KnowledgeBaseNotesSerializer
	permission_classes = [IsAuthenticated,IsOwnerNotes]
	pagination_class = ResourcesPagination
	queryset=KnowledgeBaseNotes.objects.all()
	filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
	filter_fields = ['id', 'resource']
	search_fields = ['title','slug','content']
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
	request : http://127.0.0.1:8000/api/soft-skills-notes/
    response :
    {
    "count": 1,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/soft-skills-notes/",
    "results": [
            {
                "url": "http://127.0.0.1:8000/api/soft-skills-notes/1/",
    			"id": 1,
    			"user": 1,
    			"resource": 9,
    			"title": "New",
    			"content": "new",
    			"slug": "new",
    			"created_at": "2018-03-15T09:45:10.474941Z",
    			"modified_at": "2018-03-15T09:46:54.265141Z"
            }
        ]
    }
	"""
	serializer_class = SoftSkillsDataNotesSerializer
	permission_classes = [IsAuthenticated,IsOwnerNotes]
	pagination_class = ResourcesPagination
	queryset=SoftSkillsDataNotes.objects.all()
	filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
	filter_fields = ['id', 'resource']
	search_fields = ['title','slug','content']
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
	request : http://127.0.0.1:8000/api/random-data-notes/
    response :
    {
    "count": 1,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/random-data-notes/",
    "results": [
            {
                "url": "http://127.0.0.1:8000/api/random-data-notes/1/",
    			"id": 1,
    			"user": 1,
    			"resource": 9,
    			"title": "New",
    			"content": "new",
    			"slug": "new",
    			"created_at": "2018-03-15T09:45:10.474941Z",
    			"modified_at": "2018-03-15T09:46:54.265141Z"
            }
        ]
    }
	"""
	serializer_class = RandomDataNotesSerializer
	permission_classes = [IsAuthenticated,IsOwnerNotes]
	pagination_class = ResourcesPagination
	queryset=RandomDataNotes.objects.all()
	filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
	filter_fields = ['id', 'resource']
	search_fields = ['title','slug','content']
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
