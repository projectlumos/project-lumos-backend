from rest_framework.pagination import (
    PageNumberPagination
)
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination


class ResourcesPagination(PageNumberPagination):
    """
    It handles the pagination for resources
    """
    page_size_query_param = 'page_size'
    page_size = 15


class LimitPagination(MultipleModelLimitOffsetPagination):
    """
    Pagination class for global search view.
    """
    default_limit = 15