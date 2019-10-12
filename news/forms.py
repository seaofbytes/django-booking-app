from .models import Comment
from django import forms
from django.forms import ModelForm, Textarea
from .models import Article


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class ArticleModelForm(ModelForm):

    class Meta:
        model = Article
        fields = ('__all__')
        widgets = {
            'meta': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
