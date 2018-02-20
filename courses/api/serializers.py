from rest_framework.serializers import (
    ModelSerializer,
    # SerializerMethodField,
    PrimaryKeyRelatedField,
    Field,
    # ReadOnlyField
)

from courses.models import Language, Domain, Video, ExternalLink

class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'id',
            'language_name',
            'slug',
            'languages_for'
        ]


class DomainSerializer(ModelSerializer):
    class Meta:
        model = Domain
        fields = [
            'id'
            'domain_name'
            'slug',
            'domains_for'
        ]

class VideoSerializer(ModelSerializer):
    videos_languages = PrimaryKeyRelatedField(many=True, read_only=True)  #refer to related_terms in models %(class) is replaced by child class in lower case
    videos_domains = PrimaryKeyRelatedField(many=True, read_only=True)  #refer to related_terms in models %(class) is replaced by child class in lower case
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
    externallinks_languages = PrimaryKeyRelatedField(many=True, read_only=True)  #refer to related_terms in models %(class) is replaced by child class in lower case
    externallinks_domains = PrimaryKeyRelatedField(many=True, read_only=True)  #refer to related_terms in models %(class) is replaced by child class in lower case
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
