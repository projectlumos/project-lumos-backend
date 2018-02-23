from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    Field,
)
from courses.models import Language, Domain, Video, ExternalLink


class LanguageSerializer(ModelSerializer):
    """
    serializer for Language model class
    """
    class Meta:
        model = Language
        fields = [
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
    class Meta:
        model = Domain
        fields = [
            'id'
            'domain_name'
            'slug',
            'description',
            'icon',
            'domains_for'
        ]


class VideoSerializer(ModelSerializer):
    """
    serializer for Video model class
    """
    #refer to related_terms in models %(class) is replaced by child class in lower case
    videos_languages = PrimaryKeyRelatedField(many=True, read_only=True)
    videos_domains = PrimaryKeyRelatedField(many=True, read_only=True)
    multiple_languages = Field()
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'slug',
            'videos_languages',
            'videos_domains',
            'skill_level',
            'multiple_languages',
            'video_url'
        ]


class ExternalLinkSerializer(ModelSerializer):
    """
    serializer for ExternalLink model class
    """
    #refer to related_terms in models %(class) is replaced by child class in lower case
    externallinks_languages = PrimaryKeyRelatedField(many=True, read_only=True)
    externallinks_domains = PrimaryKeyRelatedField(many=True, read_only=True)
    multiple_languages = Field()
    class Meta:
        model = ExternalLink
        fields = [
            'id',
            'title',
            'description',
            'slug',
            'externallinks_languages',
            'externallinks_domains',
            'multiple_languages',
            'external_type',
            'skill_level',
            'link_url',
            'paid'
        ]
