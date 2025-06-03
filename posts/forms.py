from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '1',
        'placeholder': 'Enter title'
    }))
    body = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
        'placeholder': 'What\'s happening?'
    }))

    class Meta:
        model = Post
        fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': '3',
        'placeholder': 'Tweet your reply'
    }))

    class Meta:
        model = Comment
        fields = ['content']