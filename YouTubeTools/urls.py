from django.urls import path
from . import views

urlpatterns = [
    path('playlist_length/', views.calculate_length_view, name='calculate_length_view'),
    # ... other URL patterns ...
]

