# framework level libraries

from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)

# app level imports

from courses.models import Language, Domain, KnowledgeBase, SoftSkills, SoftSkillsData, RandomData


language_detail_url = HyperlinkedIdentityField(
    # url to detail view
    view_name='language-detail',
    read_only=True
)

domain_detail_url = HyperlinkedIdentityField(
    view_name='domain-detail',
    read_only=True
)

softskills_detail_url = HyperlinkedIdentityField(
    view_name='softskills-detail',
    read_only=True
)

knowledgebase_detail_url = HyperlinkedIdentityField(
    view_name='knowledgebase-detail',
    read_only=True
)

softskillsdata_detail_url=HyperlinkedIdentityField(
    view_name='softskillsdata-detail',
    read_only=True
)

randomdata_detail_url=HyperlinkedIdentityField(
    view_name='randomdata-detail',
    read_only=True
)


class LanguageSerializer(ModelSerializer):
    """
    serializer for Language model class
    """
    url = language_detail_url

    class Meta:
        model = Language
        fields = [
            'url',
            'id',
            'language_name',
            'slug',
            'site_url',
            'description',
            'icon',
        ]


class DomainSerializer(ModelSerializer):
    """
    serializer for Domain model class
    """
    url = domain_detail_url

    class Meta:
        model = Domain
        fields = [
            'url',
            'id',
            'domain_name',
            'slug',
            'description',
            'icon',
        ]


class SoftSkillsSerializer(ModelSerializer):
    """
    serializer for SoftSkills model class
    """
    url = softskills_detail_url

    class Meta:
        model = SoftSkills
        fields = [
            'url',
            'id',
            'soft_skill_category',
            'slug',
            'description',
            'icon',
        ]


class SoftSkillsDataSerializer(ModelSerializer):
    """
    serializer for SoftSkillsData model class
    """
    soft_skill = SoftSkillsSerializer(many=True)
    url = softskillsdata_detail_url

    class Meta:
        model = SoftSkillsData
        fields = [
            'url',
            'id',
            'soft_skill',
            'title',
            'description',
            'slug',
            'data_type',
            'link_url',
            'paid',
            'ratings'
        ]


class KnowledgeBaseSerializer(ModelSerializer):
    """
    serializer for KnowledgeBase model class
    """
    languages = LanguageSerializer(many=True)
    domains = DomainSerializer(many=True)
    url = knowledgebase_detail_url

    class Meta:
        model = KnowledgeBase
        fields = [
            'url',
            'id',
            'title',
            'description',
            'slug',
            'languages',
            'domains',
            'data_type',
            'skill_level',
            'link_url',
            'paid',
            'project',
            'ratings'
        ]


class RandomDataSerializer(ModelSerializer):
    """
    serializer for RandomData model class
    """
    url = randomdata_detail_url

    class Meta:
        model = RandomData
        fields = [
            'url',
            'id',
            'title',
            'description',
            'slug',
            'data_type',
            'link_url',
            'paid',
            'ratings'
        ]
