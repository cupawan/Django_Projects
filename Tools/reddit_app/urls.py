
from django.urls import path
from . import views

urlpatterns = [
    path('reddit_posts/', views.get_posts_view, name='get_posts_view'),
    # ... other URL patterns ...
]
