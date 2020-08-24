from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','short_description','content')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'short_description': forms.Textarea(attrs={'class':'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

        widgets = {
            'comment':forms.Textarea(attrs={'class':'form-control'}),
        }