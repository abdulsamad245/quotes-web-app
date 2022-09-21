from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        # fields = ['title', 'image','image1']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'image' : forms.FileInput(attrs={'class' : 'form-control'})
        }
