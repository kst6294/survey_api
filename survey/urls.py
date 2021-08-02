from django.urls import path

from survey.views import ListView

urlpatterns = [
    path('', ListView.as_view())
]
