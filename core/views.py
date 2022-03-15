from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
import core.models


# Генерация title на страницах
class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


# Выводит главную страницу сайта
class IndexView(TitleMixin, TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Главная страница'


# Выводит список компании, так же есть фильтр по названию компании
class Company(TitleMixin,  ListView):
    title = 'Рейтинг компаний'

    def get_queryset(self):
        name = self.request.GET.get('name')
        queryset = core.models.Company.objects.all()
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset

# Выводит информацию о конкретной компании
class CompanyDetail(TitleMixin, DetailView):
    model = core.models.Company

    def get_title(self):
        return str(self.get_object())
