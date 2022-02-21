from django.urls import path
from .views import BlogView, PostView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
]
