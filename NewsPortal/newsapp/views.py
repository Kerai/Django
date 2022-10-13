from django.shortcuts import render

# ---------------------------------------------------------
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView, TemplateView)


from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, PermissionDenied
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


from .models import Post
from .forms import PostForm, UserForm
from .filters import PostFilter

from django.shortcuts import redirect


class OwnerPermissionRequiredMixin(PermissionRequiredMixin):

    def has_permission(self):
        perms = self.get_permission_required()
        if not self.get_object().author.authorUser.id == self.request.user.id:
            raise PermissionDenied()
        return self.request.user.has_perms(perms)


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


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('newsapp.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 1
        return super().form_valid(form)


class PostUpdate(OwnerPermissionRequiredMixin, UpdateView):
    permission_required = ('newsapp.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 1
        return super().form_valid(form)


class PostDelete(OwnerPermissionRequiredMixin, DeleteView):
    permission_required = ('newsapp.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = Post
        post.categoryType = 1
        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('newsapp.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 2
        return super().form_valid(form)


class ArticleUpdate(OwnerPermissionRequiredMixin, UpdateView):
    permission_required = ('newsapp.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_add.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 2
        return super().form_valid(form)


class ArticleDelete(OwnerPermissionRequiredMixin, DeleteView):
    permission_required = ('newsapp.delete_post',)
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = Post
        post.categoryType = 2
        return super().form_valid(form)


class ProtectedView(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    model = User
    template_name = 'userUpdate.html'

    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.kwargs['pk']})


class ProfileUserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('news')


class Welcome(LoginRequiredMixin, TemplateView):
    template_name = 'welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_Authors'] = not self.request.user.groups.filter(name='Authors').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name="Authors")
    if not request.user.groups.filter(name="Authors").exists():
        premium_group.user_set.add(user)
    return redirect('news/')


