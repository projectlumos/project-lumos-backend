from django.contrib import admin
from .models import KnowledgeBaseNotes, SoftSkillsDataNotes, RandomDataNotes
# Register your models here.


class KnowledgeBaseNotesModelAdmin(admin.ModelAdmin):
	"""
	This model admin will handle the admin panel
	for KnowledgeBaseNotes class.
	"""
	list_display = ['user', 'resource', 'title', 'is_active', 'created_at', 'modified_at']
	list_display_links = ['title']
	list_filter = ['user', 'resource', 'is_active', 'created_at', 'modified_at']
	search_fields = ['title', 'content']
	autocomplete_fields = ['user', 'resource']
	readonly_fields = ['slug']

	class Meta:
		model = KnowledgeBaseNotes


class SoftSkillsDataNotesModelAdmin(admin.ModelAdmin):
	"""
	This model admin will handle the admin panel
	for SoftSkillsDataNotes class.
	"""
	list_display = ['user', 'resource', 'title', 'is_active', 'created_at', 'modified_at']
	list_display_links = ['title']
	list_filter = ['user', 'resource', 'is_active', 'created_at', 'modified_at']
	search_fields = ['title', 'content']
	autocomplete_fields = ['user', 'resource']
	readonly_fields = ['slug']

	class Meta:
		model = SoftSkillsDataNotes


class RandomDataNotesModelAdmin(admin.ModelAdmin):
	"""
	This model admin will handle the admin panel
	for RandomData class.
	"""
	list_display = ['user', 'resource', 'title', 'is_active', 'created_at', 'modified_at']
	list_display_links = ['title']
	list_filter = ['user', 'resource', 'is_active', 'created_at', 'modified_at']
	search_fields = ['title', 'content']
	autocomplete_fields = ['user', 'resource']
	readonly_fields = ['slug']

	class Meta:
		model = RandomDataNotes


admin.site.register(KnowledgeBaseNotes, KnowledgeBaseNotesModelAdmin)
admin.site.register(SoftSkillsDataNotes, KnowledgeBaseNotesModelAdmin)
admin.site.register(RandomDataNotes, RandomDataNotesModelAdmin)





