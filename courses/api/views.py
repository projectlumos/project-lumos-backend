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
    filter_fields = ['id', 'language_name', 'slug', 'description']
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
    filter_fields = ['id', 'domain_name', 'slug', 'description']
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
    filter_fields = ['id', 'soft_skill_category', 'slug', 'description']
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
    filter_fields = ['title', 'description', 'slug', 'data_type', 'paid', 'soft_skill__id', 'soft_skill__slug']
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
    filter_fields = ['title', 'description', 'slug', 'skill_level', 'data_type', 'paid', 'languages__id',
                    'languages__slug', 'domains__id', 'domains__slug', 'project']
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
    filter_fields = ['title', 'description', 'slug', 'data_type', 'paid']
    ordering_fields = ['data_type', 'title', 'paid']
    ordering = ['data_type']
    queryset = RandomData.objects.all()

    def get_queryset(self):
        queryset = RandomData.objects.filter(is_active=True)
        return queryset
