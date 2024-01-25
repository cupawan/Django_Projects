
from django.urls import path
from . import views

urlpatterns = [
    path('bhaskar/', views.dainik_bhaskar, name='dainik_bhaskar'),
    # ... other URL patterns ...
]
