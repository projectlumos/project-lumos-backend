from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    PrimaryKeyRelatedField
)
from ratings.models import KnowledgeBaseRating, SoftSkillsDataRating, RandomDataRating


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
    user = PrimaryKeyRelatedField(read_only=True)
    resource = PrimaryKeyRelatedField(read_only=True)
    url = knowledgebase_detail_url

    class Meta:
        model = KnowledgeBaseRating
        fields = [
            'url',
            'id',
            'user',
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
    user = PrimaryKeyRelatedField(read_only=True)
    resource = PrimaryKeyRelatedField(read_only=True)
    url = softskillsdatarating_detail_url

    class Meta:
        model = SoftSkillsDataRating
        fields = [
            'url',
            'id',
            'user',
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
    user = PrimaryKeyRelatedField(read_only=True)
    resource = PrimaryKeyRelatedField(read_only=True)
    url = randomdatarating_detail_url

    class Meta:
        model = RandomDataRating
        fields = [
            'url',
            'id',
            'user',
            'resource',
            'attribute_1',
            'attribute_2',
            'attribute_3',
            'attribute_4'
        ]
