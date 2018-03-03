from django import forms
from .models import KnowledgeBase

class KnowledgeBaseForm(forms.ModelForm):
    class Meta:
        model = KnowledgeBase
        fields = '__all__'

    def clean(self):
        super(KnowledgeBaseForm, self).clean()
        languages = self.cleaned_data.get('languages', None)
        domains = self.cleaned_data.get('domains', None)
        if languages.count() == 0 and domains.count() == 0:
            raise forms.ValidationError("languages and domains both can't be empty")
        return self.cleaned_data
