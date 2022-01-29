from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('our_team', views.our_team, name='our_team'),
]
