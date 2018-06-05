from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView


class NewsListView(ListView):
    template_name = 'news/news-list.html'
    context_object_name = 'news'
    model = News


class NewsDetailView(DetailView):
    template_name = 'news/news-detail.html'
    context_object_name = 'news'
    model = News
