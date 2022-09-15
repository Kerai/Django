from django import forms
from django.core.exceptions import ValidationError


from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
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
