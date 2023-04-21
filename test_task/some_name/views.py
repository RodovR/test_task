from django.views.generic import ListView

from .models import Menu
from .utils import DataMixin


class BasePage(DataMixin, ListView):
    model = Menu
    template_name = 'some_name_pages/base_page.html'
    context_object_name = 'base'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title_name = self.get_user_data(title='Главная страница')
        return dict(list(context.items()) + list(title_name.items()))


class SecondPage(DataMixin, ListView):
    model = Menu
    template_name = 'some_name_pages/second_page.html'
    context_object_name = 'second'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title_name = self.get_user_data(title='Вторая страница')
        return dict(list(context.items()) + list(title_name.items()))


class ThirdPage(DataMixin, ListView):
    model = Menu
    template_name = 'some_name_pages/third_page.html'
    context_object_name = 'third'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title_name = self.get_user_data(title='Третья страница')
        return dict(list(context.items()) + list(title_name.items()))


class FourthPage(DataMixin, ListView):
    model = Menu
    template_name = 'some_name_pages/fourth_page.html'
    context_object_name = 'fourth'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title_name = self.get_user_data(title='Четвёртая страница')
        return dict(list(context.items()) + list(title_name.items()))
