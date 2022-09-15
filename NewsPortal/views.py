from django.shortcuts import render

# ---------------------------------------------------------
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError


from .models import Post
from .forms import PostForm
from .filters import PostFilter


class NEWS (ListView):
    model = Post
    ordering = '-dateCreation'    # sort by date
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NEWSOne(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 1
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 1
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = Post
        post.categoryType = 1
        return super().form_valid(form)


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 2
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 2
        return super().form_valid(form)


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = Post
        post.categoryType = 2
        return super().form_valid(form)



