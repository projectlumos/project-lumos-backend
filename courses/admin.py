from django.contrib import admin

# app level imports
from .models import Domain, Language, SoftSkills, SoftSkillsData, KnowledgeBase, RandomData
from .forms import KnowledgeBaseForm
# Register your models here.


class DomainModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for Domain class.
    """
    # fields to be displayed in the admin site list
    list_display = ['domain_name', 'slug']

    list_editable = ['domain_name']

    # fields which link the list object to object
    list_display_links = ['slug']

    # fields which are searchable from the admin site
    search_fields = ['domain_name', 'slug']

    # fields to filter by
    list_filter = ['domain_name']

    # this field can only be read at the admin site. slug is created when object is saved so no write permissions given
    readonly_fields = ['slug']

    class Meta:
        model = Domain


class LanguageModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for Language class.
    """
    list_display = ['language_name', 'slug']
    list_editable = ['language_name']
    list_display_links = ['slug']
    search_fields = ['language_name', 'slug']
    list_filter = ['language_name']
    readonly_fields = ['slug']

    class Meta:
        model = Language


class SoftSkillsModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for SoftSkills class.
    """
    list_display = ['soft_skill_category', 'slug']
    list_editable = ['soft_skill_category']
    list_display_links = ['slug']
    search_fields = ['soft_skill_category', 'slug']
    list_filter = ['soft_skill_category']
    readonly_fields = ['slug']

    class Meta:
        model = SoftSkills


class KnowledgeBaseModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for KnowledgeBase class.
    """
    form = KnowledgeBaseForm
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'skill_level', 'data_type', 'paid',
                    'project']
    list_display_links = ['title']

    # fields to filter by. __ indicates the attribute of a related class, by default django assumes id
    list_filter = ['is_active', 'languages__language_name', 'domains__domain_name', 'skill_level',
                    'modified_at', 'created_at', 'data_type', 'paid', 'project']

    # fields which are searchable from the admin site
    search_fields = ['title', 'description', 'languages__language_name', 'domains__domain_name']

    # this field provides a way to search for related class attributes associated, autocompletes the attribute to be
    # searched for
    autocomplete_fields = ['languages', 'domains']

    # this field can only be read at the admin site. Since multiple_languages is a property called when object is saved,
    # no write permissions given
    readonly_fields = ['slug', 'ratings']

    class Meta:
        model = KnowledgeBase


class SoftSkillsDataModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for SoftSkillsData class.
    """
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'data_type', 'paid']
    list_display_links = ['title']
    list_editable = ['is_active']
    list_filter = ['is_active', 'soft_skill__soft_skill_category', 'modified_at', 'created_at']
    search_fields = ['title', 'description', 'soft_skill__soft_skill_category']
    autocomplete_fields = ['soft_skill']
    readonly_fields = ['slug', 'ratings']

    class Meta:
        model = SoftSkillsData


class RandomDataModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for RandomData class.
    """
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'data_type', 'paid']
    list_display_links = ['title']
    list_editable = ['is_active']
    list_filter = ['is_active', 'modified_at', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['slug', 'ratings']

    class Meta:
        model = RandomData


"""Register the admin models """
admin.site.register(Domain, DomainModelAdmin)
admin.site.register(Language, LanguageModelAdmin)
admin.site.register(SoftSkills, SoftSkillsModelAdmin)
admin.site.register(KnowledgeBase, KnowledgeBaseModelAdmin)
admin.site.register(SoftSkillsData, SoftSkillsDataModelAdmin)
admin.site.register(RandomData, RandomDataModelAdmin)
