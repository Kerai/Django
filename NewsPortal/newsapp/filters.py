from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from django.forms import DateInput
from .models import Post, Author, Category


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Author',
        empty_label='Select a author',
    )

    Сategory = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Select category',
    )

    date_search = DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Later by date',
        widget=DateInput(
            format='%d-%m-%Y',
            attrs={'type': 'date'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'rating': [
                'gt',
                'lt',
                ],
            }

