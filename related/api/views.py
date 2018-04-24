# framework level libraries

from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins

# app level imports

from courses.models import SoftSkillsData, KnowledgeBase, RandomData

# api level imports
from related.api.serializers import KnowledgeBaseRelatedSerializer, SoftSkillsDataRelatedSerializer, \
    RandomDataRelatedSerializer
from courses.api.pagination import ResourcesPagination,LimitPagination



class KnowledgeBaseRelatedViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = KnowledgeBaseRelatedSerializer
    queryset = KnowledgeBase.related.all()

    # def get_queryset(self):
    #     tag_list = []
    #     instance = self.get_object()
    #     qs = KnowledgeBase.objects.filter(id=instance.id)
    #     if qs.tag.all().exists():
    #         for tag in qs.tag.all():
    #             tag_list.append(tag)
    #             for res in KnowledgeBase.objects.all():
    #                 if res.tag.all() in tag_list:
    #                     return KnowledgeBase.objects.filter(id=res.id)
    #         else:
    #             return []
    #     else:
    #         return []

    #  def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     if KnowledgeBase.objects.get(id=instance.id).tag.all().exists():
    #
    #     return Response(serializer.data)

class SoftSkillsDataRelatedViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SoftSkillsDataRelatedSerializer
    queryset = SoftSkillsData.objects.all()

    # def get_queryset(self):
    #
    #

class RandomDataRelatedViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = RandomDataRelatedSerializer
    queryset = RandomData.objects.all()

    # def get_queryset(self):
