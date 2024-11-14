from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import ArticleView, IndexView, ArticleCommentsView


urlpatterns = [
    path('', IndexView.as_view(), name='articles_index'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('<int:article_id>/comments/<int:id>/',
         ArticleCommentsView.as_view(),
         name='comments_view'),
]
