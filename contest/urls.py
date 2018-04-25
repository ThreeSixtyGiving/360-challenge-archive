from django.urls import path

from contest.views import index, submition


urlpatterns = [
    path('', index, name='contest_index'),
    path('submition', submition, name='contest_submition'),
]
