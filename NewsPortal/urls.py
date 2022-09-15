from django.urls import path
from .views import NEWS, NEWSOne, PostCreate, PostUpdate, PostDelete, ArticleCreate, ArticleDelete, ArticleUpdate


urlpatterns = [
    path('', NEWS.as_view(), name='news'),
    path('<int:pk>', NEWSOne.as_view(), name='post_view'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]
