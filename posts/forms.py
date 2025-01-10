from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['content', 'img']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text']

class searchForm(forms.Form):
	query = forms.CharField(label='Search...', max_length=100, required=False)
