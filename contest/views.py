from django.shortcuts import render


def index(request):
    return render(request, 'contest/index.html')


def submition(request):
    return render(request, 'contest/submition.html')
