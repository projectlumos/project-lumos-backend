# framework level libraries

from rest_framework.serializers import (
    ModelSerializer,
)

# app level imports

from courses.models import KnowledgeBase, SoftSkillsData, RandomData

class KnowledgeBaseRelatedSerializer(ModelSerializer):

    class Meta:
        model = KnowledgeBase
        fields = [
            'id',
            'title',
            'slug'
        ]


class SoftSkillsDataRelatedSerializer(ModelSerializer):

    class Meta:
        model = SoftSkillsData
        fields = [
            'id',
            'title',
            'slug'
        ]


class RandomDataRelatedSerializer(ModelSerializer):

    class Meta:
        model = RandomData
        fields = [
            'id',
            'title',
            'slug'
        ]
