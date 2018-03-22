from django.contrib.auth.models import User
# framework level libraries
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	PrimaryKeyRelatedField,
)

# app level imports
from notesapp.models import KnowledgeBaseNotes, SoftSkillsDataNotes, RandomDataNotes
from courses.models import KnowledgeBase, SoftSkillsData, RandomData


knowledgebasenotes_detail_url = HyperlinkedIdentityField(
    # URL to detail view
	view_name='knowledgebasenotes-detail',
	read_only=True
)

softskillsdatanotes_detail_url = HyperlinkedIdentityField(
	view_name='softskillsdatanotes-detail',
	read_only=True
)

randomdatanotes_detail_url = HyperlinkedIdentityField(
	view_name='randomdatanotes-detail',
	read_only=True
)


class KnowledgeBaseNotesSerializer(ModelSerializer):
	"""
	serializer class for KnowledgeBaseNotes model
	"""
	resource = PrimaryKeyRelatedField(queryset=KnowledgeBase.objects.all())
	url = knowledgebasenotes_detail_url

	class Meta:
		model = KnowledgeBaseNotes
		fields = [
			'url',
			'id',
			'user',
			'resource',
			'title',
			'content',
			'slug',
			'created_at',
			'modified_at',
		]

		extra_kwargs = {
			'user' : {'read_only': True},
			'created_at' : {'read_only': True},
			'modified_at' : {'read_only': True},
			'slug' : {'read_only': True}
		}


class SoftSkillsDataNotesSerializer(ModelSerializer):
	"""
	serializer class for SoftSkillsDataNotes model
	"""
	resource = PrimaryKeyRelatedField(queryset=SoftSkillsData.objects.all())
	url = softskillsdatanotes_detail_url

	class Meta:
		model = SoftSkillsDataNotes
		fields = [
			'url',
			'id',
			'user',
			'resource',
			'title',
			'content',
			'slug',
			'created_at',
			'modified_at',
		]

		extra_kwargs = {
			'user' : {'read_only': True},
			'created_at' : {'read_only': True},
			'modified_at' : {'read_only': True},
			'slug' : {'read_only': True}
		}


class RandomDataNotesSerializer(ModelSerializer):
	"""
	serializer class for RandomDataNotes model
	"""
	resource = PrimaryKeyRelatedField(queryset=RandomData.objects.all())
	url = randomdatanotes_detail_url

	class Meta:
		model = RandomDataNotes
		fields = [
			'url',
			'id',
			'user',
			'resource',
			'title',
			'content',
			'slug',
			'created_at',
			'modified_at',
		]

		extra_kwargs = {
			'user' : {'read_only': True},
			'created_at' : {'read_only': True},
			'modified_at' : {'read_only': True},
			'slug' : {'read_only': True}
		}
