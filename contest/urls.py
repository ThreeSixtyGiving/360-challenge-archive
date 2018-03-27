from django.urls import path

from contest.views import home, submition


urlpatterns = [
    path('', home, name='contest_home'),
    path('submition', submition, name='contest_submition'),
]
