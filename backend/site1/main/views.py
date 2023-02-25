from django.shortcuts import render

def index(response):
    authenticatd = False
    if response.user.is_authenticated:
        authenticatd = True
    else:
        authenticatd = False
    return render(response, "main/shop.html", {'authenticatd': authenticatd, 'response.user': response.user})

