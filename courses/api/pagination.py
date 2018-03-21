from rest_framework.pagination import (
    PageNumberPagination
)


class ResourcesPagination(PageNumberPagination):
    """
    It handles the pagination for resources
    """
    page_size_query_param = 'page_size'
    page_size = 15
