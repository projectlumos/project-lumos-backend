from django.contrib import admin
from .models import KnowledgeBaseRating, SoftSkillsDataRating, RandomDataRating
# Register your models here.


class KnowledgeBaseRatingModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for KnowledgeBase class
    """
    # fields to be displayed in the admin site list
    list_display = ['user', 'resource', 'is_active', 'created_at', 'modified_at',
                    'attribute_1', 'attribute_2', 'attribute_3', 'attribute_4']

    # fields which link the list object to object
    list_display_links = ['user', 'resource']

    # fields to filter by
    list_filter = ['user', 'resource']

    readonly_fields = ['get_avg_attribute1', 'get_avg_attribute2', 'get_avg_attribute3', 'get_avg_attribute4']

    class Meta:
        model = KnowledgeBaseRating


class SoftSkillsDataRatingModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for SoftSkillsDataRating class
    """
    list_display = ['user', 'resource', 'is_active', 'created_at', 'modified_at',
                    'attribute_1', 'attribute_2', 'attribute_3', 'attribute_4']
    list_display_links = ['user', 'resource']
    list_filter = ['user', 'resource']
    readonly_fields = ['get_avg_attribute1', 'get_avg_attribute2', 'get_avg_attribute3', 'get_avg_attribute4']
    class Meta:
        model = SoftSkillsDataRating


class RandomDataRatingModelAdmin(admin.ModelAdmin):
    """
    handles the admin panel for RandomDataRating class
    """
    list_display = ['user', 'resource', 'is_active', 'created_at', 'modified_at',
                    'attribute_1', 'attribute_2', 'attribute_3', 'attribute_4']
    list_display_links = ['user', 'resource']
    list_filter = ['user', 'resource']
    readonly_fields = ['get_avg_attribute1', 'get_avg_attribute2', 'get_avg_attribute3', 'get_avg_attribute4']
    class Meta:
        model = RandomDataRating


"""Register the admin models """
admin.site.register(KnowledgeBaseRating, KnowledgeBaseRatingModelAdmin)
admin.site.register(SoftSkillsDataRating, SoftSkillsDataRatingModelAdmin)
admin.site.register(RandomDataRating, RandomDataRatingModelAdmin)
