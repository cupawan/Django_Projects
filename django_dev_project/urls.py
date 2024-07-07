# myproject/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev/', include('TranslationApp.urls')),
    path('dev/', include('RedditApp.urls')),
    path('dev/', include('YouTubeTools.urls')),
    path('health/', include('HealthMaster.urls')),
    ]
