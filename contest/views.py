from django.shortcuts import render


def index(request):
    return render(request, 'contest/index.html')


def terms_and_conditions(request):
    return render(request, 'contest/terms-and-conditions.html')


def faq(request):
    return render(request, 'contest/faq.html')


def resources(request):
    return render(request, 'contest/resources.html')


def submission(request):
    return render(request, 'contest/submission.html')


def form(request):
    return render(request, 'contest/form.html')
