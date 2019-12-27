from django.urls import path

from .views import murr_card_list

urlpatterns = [
    path('list/', murr_card_list, name='murr_card_list'),
]
