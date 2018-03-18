# system level import
# import os

# framework level libraries
from django.db.models import Q
import itertools
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
    )
from django_filters import rest_framework as filters
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
# project level imports

# app level imports
from courses.models import Language, Domain, SoftSkills, SoftSkillsData, KnowledgeBase, \
    RandomData

# api level imports
from courses.api.serializers import LanguageSerializer, DomainSerializer, SoftSkillsSerializer, \
    SoftSkillsDataSerializer, KnowledgeBaseSerializer, RandomDataSerializer
from courses.api.pagination import ResourcesPagination


class ReadOnlyCoursesAbstractViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Base viewset
    """
    serializer_class = None
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend,SearchFilter, OrderingFilter]
    search_fields = []
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
    request : http://127.0.0.1:8000/api/language/
    response :
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "https://pl-backend-development.herokuapp.com/api/language/1/",
                "id": 1,
                "language_name": "R",
                "slug": "r",
                "site_url": "https://www.r-project.org/",
                "description": "R is a programming language and software environment for
                statistical computing and graphics supported by the R Foundation for Statistical Computing.",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/R_logo.svg/2000px-R_logo.svg.png"
            }
        ]
    }
    """
    serializer_class = LanguageSerializer
    filter_fields = ['id']
    search_fields = ['language_name','slug','description']
    ordering_fields = ['language_name']
    ordering = ['language_name']
    queryset = Language.objects.all()


class DomainViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for DomainSerializer
    request : http://127.0.0.1:8000/api/domain/
    response :
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "http://127.0.0.1:8000/api/domain/1/",
                "id": 1,
                "domain_name": "Artificial Intelligence",
                "slug": "artificial-intelligence",
                "description": "Artificial intelligence (AI, also machine intelligence, MI)
                is intelligence demonstrated by machines, in contrast to the natural intelligence
                (NI) displayed by humans and other animals.",
                "icon": "https://www.iconfinder.com/icons/1106723/ai_artificial_computer_deep_learning_intelligence_machine_learning_icon"
            }
        ]
    }
    """
    serializer_class = DomainSerializer
    filter_fields = ['id']
    search_fields = ['domain_name','slug','description']
    ordering_fields = ['domain_name']
    ordering = ['domain_name']
    queryset = Domain.objects.all()


class SoftSkillsViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for SoftSkillsSerializer
    request : http://127.0.0.1:8000/api/soft-skills/
    response :
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "http://127.0.0.1:8000/api/soft-skills/1/",
                "id": 1,
                "soft_skill_category": "Body Language",
                "slug": "body-language",
                "description": "Does this really matter? Yes it does.SIT UP STRAIGHT!",
                "icon": ""
            }
        ]
    }
    """
    serializer_class = SoftSkillsSerializer
    filter_fields = ['id']
    search_fields = ['soft_skill_category','slug','description']
    ordering_fields = ['soft_skill_category']
    ordering = ['soft_skill_category']
    queryset = SoftSkills.objects.all()


class SoftSkillsDataViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for SoftSkillsDataSerializer
    request : http://127.0.0.1:8000/api/soft-skills-data/
    response :
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
            "url": "http://127.0.0.1:8000/api/soft-skills-data/1/",
            "id": 1,
            "soft_skill": [
                2
            ],
            "title": "How to reduce and cope with stress",
            "description": "It may seem like there’s nothing you can do about stress.",
            "slug": "how-to-reduce-and-cope-with-stress",
            "data_type": "BL",
            "link_url": "https://www.helpguide.org/articles/stress/stress-management.htm",
            "paid": false
            },
        ]
    }
    """
    serializer_class = SoftSkillsDataSerializer
    filter_fields = ['data_type', 'paid', 'soft_skill__id']
    search_fields = ['title','description','slug','soft_skill__slug']
    ordering_fields = ['data_type', 'title', 'paid']
    ordering = ['data_type']
    queryset = SoftSkillsData.objects.all()

    def get_queryset(self):
        queryset = SoftSkillsData.objects.filter(is_active=True)
        return queryset


class KnowledgeBaseViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for KnowledgeBaseSerializer
    request : http://127.0.0.1:8000/api/knowledge-base/
    response :
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "http://127.0.0.1:8000/api/knowledge-base/1/",
                "id": 1,
                "title": "Testing Django Signals",
                "description": "Learn how to test Django signals",
                "slug": "testing-django-signals",
                "languages": [
                    1
                ],
                "domains": [
                    1
                ],
                "data_type": "BL",
                "skill_level": "AD",
                "link_url": "https://medium.freecodecamp.com/how-to-testing-django-signals-like-a-pro-c7ed74279311#.n5anplyc4",
                "paid": false,
                "project": false
            },
        ]
    }
    """
    serializer_class = KnowledgeBaseSerializer
    filter_fields = ['skill_level', 'data_type', 'paid', 'languages__id',
                     'domains__id', 'project']
    search_fields = ['title','description','slug','languages__slug','domains__slug']
    ordering_fields = ['skill_level', 'data_type', 'title', 'paid']
    ordering = ['skill_level', 'data_type']
    queryset = KnowledgeBase.objects.all()

    def get_queryset(self):
        queryset = KnowledgeBase.objects.filter(is_active=True)
        return queryset


class RandomDataViewSet(ReadOnlyCoursesAbstractViewSet):
    """
    handles viewset for RandomDataSerializer
    request : http://127.0.0.1:8000/api/random-data/
    response :
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "http://127.0.0.1:8000/api/random-data/1/",
                "id": 1,
                "title": "What Are Microservices?",
                "description": "The article explains in detail what does
                a microservice architecture mean and what are the use cases where it should be deployed.",
                "slug": "what-are-microservices",
                "data_type": "BL",
                "link_url": "http://microservices.io/patterns/microservices.html",
                "paid": false
            }
        ]
    }
    """
    serializer_class = RandomDataSerializer
    filter_fields = ['data_type', 'paid']
    search_fields = ['title','description','slug']
    ordering_fields = ['data_type', 'title', 'paid']
    ordering = ['data_type']
    queryset = RandomData.objects.all()

    def get_queryset(self):
        queryset = RandomData.objects.filter(is_active=True)
        return queryset

class GlobalSearchAPIViewSet(ObjectMultipleModelAPIViewSet):

    def get_querylist(self,*args, **kwargs):
        query = self.request.GET.get('query', None)
        knowledgebase_queryset = KnowledgeBase.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query)).distinct()
        domain_queryset = Domain.objects.filter(knowledgebase_domains__in=knowledgebase_queryset).distinct()
        language_queryset = Language.objects.filter(knowledgebase_languages__in=knowledgebase_queryset).distinct()
        soft_skill_queryset = SoftSkills.objects.filter(Q(slug__icontains=query)).distinct()
        soft_skill_data_queryset = SoftSkillsData.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query)).distinct()
        random_data_queryset = RandomData.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query))
        
        querylist = (
        {
            'queryset':language_queryset,
            'serializer_class': LanguageSerializer,
        },

        {
            'queryset': domain_queryset,
            'serializer_class': DomainSerializer,
        }, 

        {
            'queryset': knowledgebase_queryset,
            'serializer_class': KnowledgeBaseSerializer,
        },

        {
            'queryset': soft_skill_data_queryset,
            'serializer_class': SoftSkillsDataSerializer,
        },

        {

            'queryset': soft_skill_queryset ,
            'serializer_class': SoftSkillsSerializer,
        },

        {
            'queryset': random_data_queryset,
            'serializer_class': RandomDataSerializer,
        },

    )
        return querylist

# class GlobalSearchViewSet(viewsets.ReadOnlyModelViewSet):

    # serializer_class = GlobalSearchSerializer
   
#     def get_queryset(self,*args, **kwargs):

#         query = self.request.GET.get('query', None)
#         querylist = (
#         {
#         'queryset': KnowledgeBase.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query)).distinct(),
#         'serializer_class': KnowledgeBaseSerializer,
#         },
#         {
#         'queryset': SoftSkillsData.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query)).distinct(),
#         'serializer_class': SoftSkillsDataSerializer,
#         },
#         {

#         'queryset': SoftSkills.objects.filter(Q(slug__icontains=query)).distinct(),
#         'serializer_class': SoftSkillsSerializer,
#         },
#         {
#         'queryset': RandomData.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query)).distinct(),
#         'serializer_class': RandomDataSerializer,
#         },

#     )
#         return querylist


# class GlobalSearchViewSet(viewsets.ReadOnlyModelViewSet):
#     filter_backends = [filters.DjangoFilterBackend,SearchFilter]
#     search_fields = ['title','slug']
#     def list(self,request):
#         queryset = itertools.chain(KnowledgeBase.objects.all(),SoftSkills.objects.all(),
#             SoftSkillsData.objects.all(), RandomData.objects.all())
#         serializer_class = GlobalSearchSerializer(queryset, many = True)
#         return Response(serializer_class.data)

#     def get_queryset(self, *args, **kwargs):
#         queryset = itertools.chain(KnowledgeBase.objects.all(),SoftSkills.objects.all(),
#             SoftSkillsData.objects.all(), RandomData.objects.all())
#         return queryset


