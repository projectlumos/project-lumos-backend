# framework level libraries

from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
import operator
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


class PrerequisitesSerializer(ModelSerializer):
    """
    class for PrerequisitesSerializer
    """

    class Meta:
        model = KnowledgeBase
        fields = [
            'id',
            'title',
            'slug'
        ]


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


class SoftSkillsDataListSerializer(ModelSerializer):
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


class SoftSkillsDataDetailSerializer(ModelSerializer):
    """
    serializer for SoftSkillsData model class
    """
    soft_skill = SoftSkillsSerializer(many=True)
    url = softskillsdata_detail_url
    related = SerializerMethodField(read_only=True)

    class Meta:
        model = SoftSkillsData
        fields = [
            'url',
            'id',
            'soft_skill',
            'title',
            'description',
            'slug',
            'related',
            'data_type',
            'link_url',
            'paid',
            'ratings'
        ]

    def get_related(self, obj):
        tag_list = []
        match_count = []
        match_item_dict = {}
        result = {}
        final = []
        queryset = SoftSkillsData.objects.none()
        qs = SoftSkillsData.objects.get(id=obj.id)
        for tag in qs.tag.values_list(flat=True):
            tag_list.append(tag)
        for item in SoftSkillsData.objects.filter(is_active=True):
            item_list = []
            if item.tag.all().exists():
                for indivisual_tag in item.tag.values_list(flat=True):
                    item_list.append(indivisual_tag)
                if len(list(set(tag_list).intersection(item_list))) != 0 and item.id != obj.id:
                    match_item_dict[item.id] = len(list(set(tag_list).intersection(item_list)))
                    queryset = queryset | SoftSkillsData.objects.filter(id=item.id)
        sorted_match_item = sorted(match_item_dict.items(), key=operator.itemgetter(1), reverse=True)
        for object in sorted_match_item:
            match_count.append(object[0])
        for idx, val in enumerate(match_count):
            result['id'] = val
            obj = SoftSkillsData.objects.get(id=val)
            result['title'] = obj.title
            result['slug'] = obj.slug
            final.append(result.copy())
        return final


class KnowledgeBaseListSerializer(ModelSerializer):
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


class KnowledgeBaseDetailSerializer(ModelSerializer):
    """
    serializer for KnowledgeBase model class
    """
    languages = LanguageSerializer(many=True)
    domains = DomainSerializer(many=True)
    url = knowledgebase_detail_url
    prerequisites = PrerequisitesSerializer(many=True)
    related = SerializerMethodField(read_only=True)

    class Meta:
        model = KnowledgeBase
        fields = [
            'url',
            'id',
            'title',
            'description',
            'slug',
            'prerequisites',
            'related',
            'languages',
            'domains',
            'data_type',
            'skill_level',
            'link_url',
            'paid',
            'project',
            'ratings'
        ]

    def get_related(self, obj):
        tag_list = []
        match_count = []
        match_item_dict = {}
        result = {}
        final = []
        queryset = KnowledgeBase.objects.none()
        qs = KnowledgeBase.objects.get(id=obj.id)
        for tag in qs.tag.values_list(flat=True):
            tag_list.append(tag)
        for item in KnowledgeBase.objects.filter(is_active=True):
            item_list = []
            if item.tag.all().exists():
                for indivisual_tag in item.tag.values_list(flat=True):
                    item_list.append(indivisual_tag)
                if len(list(set(tag_list).intersection(item_list))) != 0 and item.id != obj.id:
                    match_item_dict[item.id] = len(list(set(tag_list).intersection(item_list)))
                    queryset = queryset | KnowledgeBase.objects.filter(id=item.id)
        sorted_match_item = sorted(match_item_dict.items(), key=operator.itemgetter(1), reverse=True)
        for object in sorted_match_item:
            match_count.append(object[0])
        for idx, val in enumerate(match_count):
            result['id'] = val
            obj = KnowledgeBase.objects.get(id=val)
            result['title'] = obj.title
            result['slug'] = obj.slug
            final.append(result.copy())
        return final


class RandomDataListSerializer(ModelSerializer):
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


class RandomDataDetailSerializer(ModelSerializer):
    """
    serializer for RandomData model class
    """
    url = randomdata_detail_url
    related = SerializerMethodField(read_only=True)

    class Meta:
        model = RandomData
        fields = [
            'url',
            'id',
            'title',
            'description',
            'slug',
            'related',
            'data_type',
            'link_url',
            'paid',
            'ratings'
        ]

    def get_related(self, obj):
        tag_list = []
        match_count = []
        match_item_dict = {}
        result = {}
        final = []
        queryset = RandomData.objects.none()
        qs = RandomData.objects.get(id=obj.id)
        for tag in qs.tag.values_list(flat=True):
            tag_list.append(tag)
        for item in RandomData.objects.filter(is_active=True):
            item_list = []
            if item.tag.all().exists():
                for indivisual_tag in item.tag.values_list(flat=True):
                    item_list.append(indivisual_tag)
                if len(list(set(tag_list).intersection(item_list))) != 0 and item.id != obj.id:
                    match_item_dict[item.id] = len(list(set(tag_list).intersection(item_list)))
                    queryset = queryset | RandomData.objects.filter(id=item.id)
        sorted_match_item = sorted(match_item_dict.items(), key=operator.itemgetter(1), reverse=True)
        for object in sorted_match_item:
            match_count.append(object[0])
        for idx, val in enumerate(match_count):
            result['id'] = val
            obj = RandomData.objects.get(id=val)
            result['title'] = obj.title
            result['slug'] = obj.slug
            final.append(result.copy())
        return final
