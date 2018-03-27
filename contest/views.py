from django.shortcuts import render


def home(request):
    return render(request, 'contest/home.html')


def submition(request):
    return render(request, 'contest/submition.html')
