from django.contrib import admin
from .models import Domain, Language, Video, ExternalLink
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


class VideoModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for Video class.
    """
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'skill_level', 'multi_language']
    list_display_links = ['title']

    # fields to filter by. __ indicates the attribute of a related class, by default django assumes id
    list_filter = ['is_active', 'languages__language_name', 'domains__domain_name', 'skill_level', 'modified_at',
                   'created_at']

    # fields which are searchable from the admin site
    search_fields = ['title', 'description', 'languages__language_name', 'domains__domain_name']

    # this field provides a way to search for related class attributes associated, autocompletes the attribute to be
    # searched for
    autocomplete_fields = ['languages', 'domains']

    # this field can only be read at the admin site. Since multiple_languages is a property called when object is saved,
    # no write permissions given
    readonly_fields = ['multiple_languages', 'slug']

    class Meta:
        model = Video


class ExternalLinkModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for ExternalLink class.
    """
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'skill_level', 'multi_language']
    list_display_links = ['title']
    list_editable = ['is_active', 'skill_level']
    list_filter = ['is_active', 'languages__language_name',
                   'domains__domain_name', 'skill_level', 'modified_at', 'created_at']
    search_fields = ['title', 'description', 'languages__language_name', 'domains__domain_name']
    autocomplete_fields = ['languages', 'domains']
    readonly_fields = ['multiple_languages', 'slug']

    class Meta:
        model = ExternalLink


"""Register the admin models """
admin.site.register(Domain, DomainModelAdmin)
admin.site.register(Language, LanguageModelAdmin)
admin.site.register(Video, VideoModelAdmin)
admin.site.register(ExternalLink, ExternalLinkModelAdmin)
