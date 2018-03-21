from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    PrimaryKeyRelatedField
)

from feedback.models import Feedback
from django.contrib.auth.models import User


feedback_detail_url = HyperlinkedIdentityField(
    # Url to detail view
    view_name='feedback-detail',
    read_only=True
)


class FeedbackSerializer(ModelSerializer):
	"""
	Serializer class for feedback model.
	"""
	url = feedback_detail_url

	class Meta:
		model = Feedback
		fields = [
			'url',
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