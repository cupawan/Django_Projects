# myproject/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev/', include('translate_app.urls')),
    path('dev/', include('reddit_app.urls')),
    path('dev/', include('youtube_tool_app.urls'))
    ]
