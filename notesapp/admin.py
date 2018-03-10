from django.contrib import admin
from .models import KnowledgeBaseNotes, SoftSkillsDataNotes, RandomDataNotes
# Register your models here.


class KnowledgeBaseNotesAdmin(admin.ModelAdmin):
	"""
	This model admin will handle the admin panel
	for KnowledgeBaseNotes class.
	"""
	list_display = ['user','resource','title']
	list_display_links = ['user', 'resource']
	search_fields = ['title', 'created_date','date_modified']
	readonly_fields = ['created_date','date_modified']

	class Meta:
		model = KnowledgeBaseNotes


class SoftSkillsDataNotesAdmin(admin.ModelAdmin):
	"""
	This model admin will handle the admin panel
	for SoftSkillsDataNotes class.
	"""
	list_display = ['user','resource','title']
	list_display_links = ['user', 'resource']
	search_fields = ['title', 'created_date','date_modified']
	readonly_fields = ['created_date','date_modified']

	class Meta:
		model = SoftSkillsDataNotes


class RandomDataNotesAdmin(admin.ModelAdmin):
	"""
	This model admin will handle the admin panel
	for RandomData class.
	"""
	list_display = ['user','resource','title']
	list_display_links = ['user', 'resource']
	search_fields = ['title', 'created_date','date_modified']
	readonly_fields = ['created_date','date_modified']

	class Meta:
		model = RandomDataNotes


admin.site.register(KnowledgeBaseNotes, KnowledgeBaseNotesAdmin)
admin.site.register(SoftSkillsDataNotes, KnowledgeBaseNotesAdmin)
admin.site.register(RandomDataNotes, RandomDataNotesAdmin)





