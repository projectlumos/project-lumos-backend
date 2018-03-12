from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    PrimaryKeyRelatedField
)
from ratings.models import KnowledgeBaseRating, SoftSkillsDataRating, RandomDataRating
from courses.models import KnowledgeBase, SoftSkillsData, RandomData
from django.contrib.auth.models import User


knowledgebaserating_detail_url = HyperlinkedIdentityField(
    #url to detail view
    view_name='knowledgebaserating-detail',
    read_only=True
)

softskillsdatarating_detail_url = HyperlinkedIdentityField(
    view_name='softskillsdatarating-detail',
    read_only=True
)

randomdatarating_detail_url = HyperlinkedIdentityField(
    view_name='randomdatarating-detail',
    read_only=True
)


class KnowledgeBaseRatingSerializer(ModelSerializer):
    """
    serializer for KnowledgeBaseRating
    """
    resource = PrimaryKeyRelatedField(queryset=KnowledgeBase.objects.all())
    url = knowledgebaserating_detail_url

    class Meta:
        model = KnowledgeBaseRating
        fields = [
            'url',
            'id',
            'resource',
            'attribute_1',
            'attribute_2',
            'attribute_3',
            'attribute_4'
        ]


class SoftSkillsDataRatingSerializer(ModelSerializer):
    """
    serializer for SoftSkillsDataRating
    """
    resource = PrimaryKeyRelatedField(queryset=SoftSkillsData.objects.all())
    url = softskillsdatarating_detail_url

    class Meta:
        model = SoftSkillsDataRating
        fields = [
            'url',
            'id',
            'resource',
            'attribute_1',
            'attribute_2',
            'attribute_3',
            'attribute_4'
        ]


class RandomDataRatingSerializer(ModelSerializer):
    """
    serializer for RandomDataRating
    """
    resource = PrimaryKeyRelatedField(queryset=RandomData.objects.all())
    url = randomdatarating_detail_url

    class Meta:
        model = RandomDataRating
        fields = [
            'url',
            'id',
            'resource',
            'attribute_1',
            'attribute_2',
            'attribute_3',
            'attribute_4'
        ]
