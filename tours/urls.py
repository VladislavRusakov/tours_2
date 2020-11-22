from django.urls import path

from .views import main_view, not_found_handler


handler404 = not_found_handler


urlpatterns = [
    path('', main_view, name='main'),
]
