from django.contrib import admin
from .models import Domain, Language, Video, ExternalLink
# Register your models here.

class DomainModelAdmin(admin.ModelAdmin):
    list_display = ['domain_name','__str__']
    list_display_links = ['domain_name','__str__']
    search_fields = ['domain_name','__str__']
    list_filter = ['domain_name']
    readonly_fields = ['slug']

    class Meta:
        model = Domain


class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ['language_name','__str__']
    list_display_links = ['language_name','__str__']
    search_fields = ['language_name','__str__']
    list_filter = ['language_name']
    readonly_fields = ['slug']

    class Meta:
        model = Language


class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'skill_level', 'multi_language']
    list_display_links = ['title']
    list_filter = ['is_active', 'languages__language_name', 'domains__domain_name', 'skill_level', 'modified_at', 'created_at']
    search_fields = ['title', 'description', 'languages__language_name', 'domains__domain_name']
    autocomplete_fields = ['languages', 'domains']   #should I use autocomplete_fields instead?
    readonly_fields = ['multiple_languages', 'slug']

    class Meta:
        model = Video


class ExternalLinkModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'modified_at', 'created_at', 'skill_level', 'multi_language']
    list_display_links = ['title']
    list_filter = ['is_active', 'languages__language_name', 'domains__domain_name', 'skill_level', 'modified_at', 'created_at']
    search_fields = ['title', 'description', 'languages__language_name', 'domains__domain_name']
    autocomplete_fields = ['languages', 'domains']
    readonly_fields = ['multiple_languages', 'slug']

    class Meta:
        model = ExternalLink

admin.site.register(Domain, DomainModelAdmin)
admin.site.register(Language, LanguageModelAdmin)
admin.site.register(Video, VideoModelAdmin)
admin.site.register(ExternalLink, ExternalLinkModelAdmin)
