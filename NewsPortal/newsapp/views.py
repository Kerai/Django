from django.shortcuts import render

# ---------------------------------------------------------
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class NEWS (ListView):
    model = Post
    ordering = '-dateCreation'    # sort by date
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class NEWSOne(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'