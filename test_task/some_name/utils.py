from .models import Menu

menu = [
    {'title': 'Базовая страница', 'url_name': 'base'},
    {'title': 'Вторая страница', 'url_name': 'second'},
    {'title': 'Третья страница', 'url_name': 'third'},
    {'title': 'Четвёртая страница', 'url_name': 'fourth'},
]


class DataMixin:
    def get_user_data(self, **kwargs):
        context = kwargs
        model = Menu.objects.all()
        context['model'] = model
        context['menu'] = menu
        return context
