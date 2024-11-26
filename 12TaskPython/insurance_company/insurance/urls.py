from django.urls import path
from .views import home, add_client


urlpatterns = [
    path('', home, name='home'),
    path('add/', add_client, name='add_client'),
    path('add_policy/', add_policy, name='add_policy'),
    path('add_claim/', add_claim, name='add_claim'),
]