from django.contrib import admin
from django.urls    import path, include
from core.views import ping

urlpatterns = [
    path('admin', admin.site.urls),
    path('ping', ping),
    path('survey', include('survey.urls')),
]
