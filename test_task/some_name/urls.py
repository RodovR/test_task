from django.urls import path

from .views import BasePage, SecondPage, ThirdPage, FourthPage

urlpatterns = [
    path('', BasePage.as_view(), name='base'),
    path('second_page/', SecondPage.as_view(), name='second'),
    path('third_page/', ThirdPage.as_view(), name='third'),
    path('fourth_page/', FourthPage.as_view(), name='fourth'),
]