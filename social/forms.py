from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label= '',required= False,
        widget= forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )
    image = forms.ImageField(required= False)
    class Meta:
        model = Post
        fields = ['body', 'image']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label= '',
        widget= forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )
    class Meta:
        model = Comment
        fields = ['comment']

DEMO_CHOICES =(
    ("1", "Naveen"),
    ("2", "Pranav"),
    ("3", "Isha"),
    ("4", "Saloni"),
)

