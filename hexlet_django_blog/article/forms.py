from django.shortcuts import render
from django import forms
from django.forms import ModelForm

from hexlet_django_blog.article.models import Article
    

class ArticleForm(ModelForm):
    name = forms.CharField(min_length=5, required=True)
    body = forms.CharField(min_length=10, required=True)

    class Meta:
        model = Article
        fields = ['name', 'body']
