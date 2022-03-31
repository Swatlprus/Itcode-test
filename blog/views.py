from django.shortcuts import render
import blog.models
from django.views.generic import ListView, DetailView

# Генерация title на страницах
class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context

class PostListView(TitleMixin, ListView):
    title = 'Блог'
    model = blog.models.Post

class PostDetailView(TitleMixin, DetailView):
    model = blog.models.Post

    def get_title(self):
        return str(self.get_object())