from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def main(request):
    # response = "Hello, I am your first request!"
    # return HttpResponse(response)

    return render(request, 'travel_buddy/main.html')


def travels(request):
    return render(request, 'travel_buddy/travels.html')

def destination(request):
    return render(request, 'travel_buddy/destination.html')

def add(request):
    return render(request, 'travel_buddy/add.html')

#login_required stops view without authentication
# @login_required(login_url="login/")
# def home(request):
#     return render(request, "home.html")
