from django.urls import path

from contest.views import home


urlpatterns = [
    path('', home),
]