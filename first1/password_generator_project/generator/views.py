import random
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello")
    lst = list(range(6, 25))
    print(lst)
    return render(request, "generator/home.html", {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get("uppercase"):
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get("number"):
        char.extend([chr(i) for i in range(48, 58)])

    if request.GET.get("special"):
        char.extend([chr(i) for i in range(33, 48)])

    psw = ''
    print(char)
    length = int(request.GET.get('length'))
    for i in range(length):
        psw += random.choice(char)
    return render(request, "generator/password.html", {'password': psw})


def about(request):
    return render(request, "generator/about.html", {'about': about})
