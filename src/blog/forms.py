from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'col': 120}))
    active = forms.BooleanField()
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]
