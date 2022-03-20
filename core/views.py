from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
import core.models
import core.forms
import core.filters


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

    def get_filters(self):
        return core.filters.CompanyFilter(self.request.GET)

    def get_queryset(self):

        # name = self.request.GET.get('name')
        # queryset = core.models.Company.objects.all()
        # if name:
        #     queryset = queryset.filter(name__contains=name)
        # return queryset

        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        #context['form'] = core.forms.CompanySearch(self.request.GET or None)
        context['filters'] = self.get_filters()
        return context

# Выводит информацию о конкретной компании
class CompanyDetail(TitleMixin, DetailView):
    model = core.models.Company

    def get_title(self):
        return str(self.get_object())

class CompanyUpdate(TitleMixin, UpdateView):
    model = core.models.Company
    form_class = core.forms.CompanyEdit

    def get_title(self):
        return f'Изменение данных компании "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('core:company_list')

class CompanyCreate(TitleMixin, CreateView):
    model = core.models.Company
    form_class = core.forms.CompanyEdit
    title = 'Добавление компании'

    def get_succes_url(self):
        return reverse('core:company_list')

class CompanyDelete(TitleMixin, DeleteView):
    model = core.models.Company

    def get_title(self):
        return f'Удаление книги {str(self.get_object())}'

    def get_succes_url(self):
        return reverse('core:company_list')