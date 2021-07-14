from django import forms
from uploadfileapp.models import Document


class DocumentForm(forms.ModelForm):
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 4:
            raise forms.ValidationError("enter valid description")
        return description

    class Meta:
        model = Document
        fields = ('description', 'document')
