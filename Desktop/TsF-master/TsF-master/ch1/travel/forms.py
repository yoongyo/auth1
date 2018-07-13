from .models import Post
from django import forms



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'name',
            'title',
            'content',
            'language',
            'visited_country',
            'next_country',
            'guide_at',
            'email',
            'interest',
            'img',
            'time',
            'price',
            'local'
        }

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
