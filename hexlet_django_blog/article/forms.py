from django.shortcuts import render
from django import forms
from django.forms import ModelForm

from hexlet_django_blog.article.models import Article
    

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return name
    
    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body) < 10:
            raise  forms.ValidationError('Body must be at least 10 characters long.')
        return  body
