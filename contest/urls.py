from django.urls import path

from contest.views import index, terms_and_conditions, faq, resources, submission, submit, thanks, cookie_usage


urlpatterns = [
    path('', index, name='contest_index'),
    path('terms-and-conditions', terms_and_conditions, name='contest_terms_and_conditions'),
    path('faq', faq, name='contest_faq'),
    path('cookie-usage', cookie_usage, name='contest_cookie_usage'),
    path('resources', resources, name='contest_resources'),
    path('submission/<int:id>', submission, name='contest_submission'),
    path('submit', submit, name='contest_submit'),
    path('thanks', thanks, name='contest_thanks'),
]
