from django.contrib import admin
from .models import Domain, Language, Video, ExternalLink
# Register your models here.

class DomainModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for Domain class.
    """
    list_display = ['domain_name','__str__']  #fields to be displayed in the admin site list
    list_display_links = ['domain_name','__str__']  #fields which link the list object to object
    search_fields = ['domain_name','__str__']  #fields which are searchable from the admin site
    list_filter = ['domain_name']  #fields to filter by
    readonly_fields = ['slug']  #this field can only be read at the admin site. slug is created when object is saved so no write permissions given

    class Meta:
        model = Domain  #indicates the model this class works for


class LanguageModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for Language class.
    """
    list_display = ['language_name','__str__']  #fields to be displayed in the admin site list
    list_display_links = ['language_name','__str__']  #fields which link the list object to object
    search_fields = ['language_name','__str__']  #fields which are searchable from the admin site
    list_filter = ['language_name']  #fields to filter by
    readonly_fields = ['slug']   #this field can only be read at the admin site. slug is created when object is saved so no write permissions given

    class Meta:
        model = Language  #indicates the model this class works for


class VideoModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for Video class.
    """
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'skill_level', 'multi_language']   #fields to be displayed in the admin site list
    list_display_links = ['title']  #fields which link the list object to object
    list_filter = ['is_active', 'languages__language_name', 'domains__domain_name', 'skill_level', 'modified_at', 'created_at']  #fields to filter by. __ indicates the attribute of a related class, by default django assumes id
    search_fields = ['title', 'description', 'languages__language_name', 'domains__domain_name']  #fields which are searchable from the admin site
    autocomplete_fields = ['languages', 'domains']  #this field provides a way to search for related class attributes associated, autocompletes the attribute to be searched for
    readonly_fields = ['multiple_languages', 'slug']  #this field can only be read at the admin site. Since multiple_languages is a property called when object is saved, no write permissions given

    class Meta:
        model = Video  #indicates the model this class works for


class ExternalLinkModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for ExternalLink class.
    """
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'skill_level', 'multi_language']   #fields to be displayed in the admin site list
    list_display_links = ['title']  #fields which link the list object to object
    list_filter = ['is_active', 'languages__language_name', 'domains__domain_name', 'skill_level', 'modified_at', 'created_at']  #fields to filter by. __ indicates the attribute of a related class, by default django assumes id
    search_fields = ['title', 'description', 'languages__language_name', 'domains__domain_name']  #fields which are searchable from the admin site
    autocomplete_fields = ['languages', 'domains']  #this field provides a way to search for related class attributes associated, autocompletes the attribute to be searched for
    readonly_fields = ['multiple_languages', 'slug']  #this field can only be read at the admin site. Since multiple_languages is a property called when object is saved, no write permissions given

    class Meta:
        model = ExternalLink  #indicates the model this class works for

"""Register the admin models """
admin.site.register(Domain, DomainModelAdmin)
admin.site.register(Language, LanguageModelAdmin)
admin.site.register(Video, VideoModelAdmin)
admin.site.register(ExternalLink, ExternalLinkModelAdmin)
