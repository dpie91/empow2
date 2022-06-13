from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Metadata:
        model = Comment
        fields = ('name', 'email', 'body')
