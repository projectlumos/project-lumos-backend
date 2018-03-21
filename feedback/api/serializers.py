from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    PrimaryKeyRelatedField
)

from feedback.models import Feedback
from django.contrib.auth.models import User


class FeedbackSerializer(ModelSerializer):
	"""
	Serializer class for feedback model.
	"""
	class Meta:
		model = Feedback
		fields = [
			'id',
			'user',
			'text',
			'created_at',
			'modified_at'
		]

		extra_kwargs = {
			'user' : {'read_only': True},
			'created_at' : {'read_only': True},
			'modified_at' : {'read_only': True},
		}