from .models import Comment, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'status', 'imageUrl')
        widgets = {            
            'imageUrl': forms.FileInput(attrs={'class': 'form-control bg-info'}),
        }    
   

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'content',)