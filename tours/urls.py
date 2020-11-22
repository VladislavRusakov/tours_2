from django.urls import path
from .views import MainView, NotFoundHandler


handler404 = NotFoundHandler


urlpatterns = [
    path('', MainView, name='main'),
]
