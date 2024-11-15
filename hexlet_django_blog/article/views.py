from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.forms import ArticleForm
from hexlet_django_blog.article.models import Article
from django.contrib import messages


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):
    
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article created successfully!')
            return redirect('articles_index')
        else:
            messages.error(request, 'There was an error in the form, please try again.')
            return render(request, 'articles/create.html', {'form': form})
            

class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        # comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])
        pass
        # return render( ... )