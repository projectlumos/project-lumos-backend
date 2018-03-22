from django.contrib import admin
from .models import Feedback
# Register your models here.

class FeedbackModelAdmin(admin.ModelAdmin):
 	"""
	handles the admin panel for feedback model.
 	"""
 	list_display = ['user', 'text', 'is_active', 'created_at', 'modified_at']
 	list_display_links = ['user']
 	list_filter = ['user']
 	search_fields = ['text']
 	autocomplete_fields = ['user']

 	class Meta:
 		model = Feedback


admin.site.register(Feedback, FeedbackModelAdmin)



