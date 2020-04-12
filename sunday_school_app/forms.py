from blog_app.models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs= {
        'class': 'form-control',
        'placeholder': 'Type your Comment',
        'rows':6,
    }))

    class Meta:
        model = Comment
        fields = ('content',)