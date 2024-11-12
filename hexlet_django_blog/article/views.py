from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class ArticleIndexView(View):

    def get(self, request, *args, **kwargs):
        tags = kwargs.get('tags')
        article_id = kwargs.get('article_id')
        if tags and article_id:
            return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
