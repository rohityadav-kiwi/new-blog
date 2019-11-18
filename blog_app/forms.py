from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, BlogPost


class SignUpForm(UserCreationForm):
    phone = forms.IntegerField(help_text='enter your number')
    email = forms.EmailField(help_text='enter your email')

    class Meta:
        model = User
        fields = ('username','phone','email','password1', 'password2', )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignUpForm, self).save(commit=False)
        user.save()
        user_profile = Profile(user=user, phone=self.cleaned_data['phone'], email = self.cleaned_data['email'])
        user.save()
        user_profile.save()
        return user, user_profile


class BlogPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super(BlogPostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BlogPost
        fields = ('title', 'post_content',)
        widgets = {'author': forms.HiddenInput()}

    def save(self, commit=True):
        instance = super(BlogPostForm, self).save(commit=False)
        instance.author = self.author
        instance.save()
        return self