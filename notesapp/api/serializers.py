from rest_framework.serializers import ( 
	ModelSerializer,
	HyperlinkedIdentityField,
	PrimaryKeyRelatedField,
)
from notesapp.model import KnowledgeBaseNotes, SoftSkillsDataNotes, RandomDataNotes
						   


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
	knowledge_base_notes = PrimaryKeyRelatedField(many=True, read_only=True)
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
	soft_skills_data_notes = PrimaryKeyRelatedField(many=True, read_only=True)
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
	random_data_notes = PrimaryKeyRelatedField(many=True, read_only=True)
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