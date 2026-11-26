from django.shortcuts import render, HttpResponse

def loadingscreen(request):
    return render(request, "loading.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

def galerie(request):
    return render(request, "galerie.html")

def universities(request):
    return render(request, "universities.html")

def chatbot(request):
    return render(request, "chatbot.html")

def bootstrap_gallery(request):
    return render(request, "bootstrap-gallery.html")