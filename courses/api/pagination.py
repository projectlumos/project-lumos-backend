from rest_framework.pagination import (
    PageNumberPagination
)


class VideoPageNumberPagination(PageNumberPagination):
    page_size = 15

class ExternalLinkPageNumberPagination(PageNumberPagination):
    page_size = 15
