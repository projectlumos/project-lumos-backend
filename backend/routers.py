from rest_framework import routers
from courses.api.views import (
    LanguageViewSet,
    DomainViewSet,
    SoftSkillsViewSet,
    SoftSkillsDataViewSet,
    KnowledgeBaseViewSet,
    RandomDataViewSet
)

router = routers.SimpleRouter()
router.register(r'language', LanguageViewSet)
router.register(r'domain', DomainViewSet)
router.register(r'soft-skills', SoftSkillsViewSet)
router.register(r'soft-skills-data', SoftSkillsDataViewSet)
router.register(r'knowledge-base', KnowledgeBaseViewSet)
router.register(r'random-data', RandomDataViewSet)
