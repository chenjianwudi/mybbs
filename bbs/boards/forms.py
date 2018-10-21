from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from boards.models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': '想说些什么'}),
                              max_length=4000,
                              help_text='最多4000字')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]