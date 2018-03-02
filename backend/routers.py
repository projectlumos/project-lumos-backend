from rest_framework import routers
from courses.api.views import (
    LanguageViewSet,
    DomainViewSet,
    VideoViewSet,
    ExternalLinkViewSet
)

router = routers.SimpleRouter()
router.register(r'language', LanguageViewSet)
router.register(r'domain', DomainViewSet)
router.register(r'video', VideoViewSet)
router.register(r'external-link', ExternalLinkViewSet)
