from rest_framework import routers
from courses.api.views import (
    LanguageViewSet,
    DomainViewSet,
    SoftSkillsViewSet,
    SoftSkillsDataViewSet,
    KnowledgeBaseViewSet,
    RandomDataViewSet
)
from ratings.api.views import(
    KnowledgeBaseRatingViewSet,
    SoftSkillsDataRatingViewSet,
    RandomDataRatingViewSet
)

from notesapp.api.views import (
	KnowledgeBaseNotesViewset,
	SoftSkillsDataNotesViewset,
	RandomDataNotesViewset
)

router = routers.SimpleRouter()
router.register(r'language', LanguageViewSet)
router.register(r'domain', DomainViewSet)
router.register(r'soft-skills', SoftSkillsViewSet)
router.register(r'soft-skills-data', SoftSkillsDataViewSet)
router.register(r'knowledge-base', KnowledgeBaseViewSet)
router.register(r'random-data', RandomDataViewSet)
router.register(r'knowledge-base-rating', KnowledgeBaseRatingViewSet)
router.register(r'softskills-data-rating', SoftSkillsDataRatingViewSet)
router.register(r'random-data-rating', RandomDataRatingViewSet)
router.register(r'knowledge-base-notes', KnowledgeBaseNotesViewset)
router.register(r'soft-skills-notes', SoftSkillsDataNotesViewset)
router.register(r'random-data-notes', RandomDataNotesViewset)
