from django.urls import path
from . import views

urlpatterns = [
    path('tigers/', views.tigers, name='tigers'),
    path('juniors/', views.juniors, name='juniors'),
    path('seniors/', views.seniors, name='seniors'),
    path('ladies/', views.ladies, name='ladies'),
]
