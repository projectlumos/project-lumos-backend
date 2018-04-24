from django.db import models

class KnowledgeBaseRelatedQuerySet(models.QuerySet):
    """
    model QuerySet for KnowledgeBase
    """
    def get_related(self):
        if self.exists():
            queryset = KnowledgeBase.objects.filter(is_active=True)
            for qs in queryset:
                if qs.knowledgebase_tag.all().exists():
                    return KnowledgeBase.objects.filter(id=qs.id)





class KnowledgeBaseRelatedManager(models.Manager):
    """
    model manager for KnowledgeBase
    """
    def get_queryset(self):
        return KnowledgeBaseRelatedQuerySet(self.model, using=self._db)

    def get_related(self):
        return self.get_queryset().get_related()
