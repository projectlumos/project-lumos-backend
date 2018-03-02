from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    PrimaryKeyRelatedField,
    ReadOnlyField,
)
from courses.models import Language, Domain, Video, ExternalLink


language_detail_url = HyperlinkedIdentityField(
    #url to detail view
    view_name='language-detail',
    read_only=True
)

domain_detail_url = HyperlinkedIdentityField(
    view_name='domain-detail',
    read_only=True
)

video_detail_url = HyperlinkedIdentityField(
    view_name='video-detail',
    read_only=True
)

externallink_detail_url=HyperlinkedIdentityField(
    view_name='externallink-detail',
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
            'languages_for'
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
            'domains_for'
        ]


class VideoSerializer(ModelSerializer):
    """
    serializer for Video model class
    """
    languages = PrimaryKeyRelatedField(many=True, read_only=True)
    domains = PrimaryKeyRelatedField(many=True, read_only=True)
    multiple_languages = ReadOnlyField()
    url = video_detail_url
    class Meta:
        model = Video
        fields = [
            'url',
            'id',
            'title',
            'description',
            'slug',
            'languages',
            'domains',
            'skill_level',
            'multiple_languages',
            'video_url'
        ]


class ExternalLinkSerializer(ModelSerializer):
    """
    serializer for ExternalLink model class
    """
    languages = PrimaryKeyRelatedField(many=True, read_only=True)
    domains = PrimaryKeyRelatedField(many=True, read_only=True)
    multiple_languages = ReadOnlyField()
    url = externallink_detail_url
    class Meta:
        model = ExternalLink
        fields = [
            'url',
            'id',
            'title',
            'description',
            'slug',
            'languages',
            'domains',
            'multiple_languages',
            'external_type',
            'skill_level',
            'link_url',
            'paid'
        ]
