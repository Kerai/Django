from .models import Post
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group


from allauth.account.forms import SignupForm



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            # 'author',
            'categoryType',
            'title',
            'text',
            'postCategory',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if description is not None and len(description) < 20:
            raise ValidationError({
               'description': 'Description cant be less than 20 symbols.'
           })
        name = cleaned_data.get('title')
        if name == description:
           raise ValidationError(
               'Description cant be identical to Title'
           )
        return cleaned_data


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',

        ]


class SignupForm(SignupForm):

    def save(self, reqest):
        user = super(SignupForm, self).save(reqest)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user



