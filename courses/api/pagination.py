from rest_framework.pagination import (
    PageNumberPagination
)


class VideoPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 15
    max_page_size = 50


class ExternalLinkPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 15
    max_page_size = 50