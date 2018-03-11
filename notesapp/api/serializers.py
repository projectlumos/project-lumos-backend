from rest_framework.serializers import ( 
	ModelSerializer,
	HyperlinkedIdentityField,
	PrimaryKeyRelatedField,
)
from notesapp.model import KnowledgeBaseNotes, SoftSkillsDataNotes, RandomDataNotes
from courses.models import KnowledgeBase, SoftSkillsData, RandomData
from django.contrib.auth.models import User



knowledgebasenotes_detail_url = HyperlinkedIdentityField(
    # URL to detail view
    view_name='knowledgebasenotes-detail',
    read_only=True
)

softskillsdatanotes_detail_url = HyperlinkedIdentityField(
    # URL to detail view
    view_name='softskillsdatanotes-detail',
    read_only=True
)

randomdatanotes_detail_url = HyperlinkedIdentityField(
    # URL to detail view
    view_name='randomdatanotes-detail',
    read_only=True
)


class KnowledgeBaseNotesSerializer(ModelSerializer):
	"""
	serializer class for KnowledgeBaseNotes model
	"""
	user = PrimaryKeyRelatedField(queryset=User.objects.all())
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
		'created_at' : {'read_only': True},
		'modified_at' : {'read_only': True}
		}


class SoftSkillsDataNotesSerializer(ModelSerializer):
	"""
	serializer class for SoftSkillsDataNotes model
	"""
	user = PrimaryKeyRelatedField(queryset=User.objects.all())
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
		'created_at' : {'read_only': True},
		'modified_at' : {'read_only': True}
		}


class RandomDataNotesSerializer(ModelSerializer):
	"""
	serializer class for RandomDataNotes model
	"""
	user = PrimaryKeyRelatedField(queryset=User.objects.all())
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
		'created_at' : {'read_only': True},
		'modified_at' : {'read_only': True}
		}