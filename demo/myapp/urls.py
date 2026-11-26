from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadingscreen, name='loadingscreen'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('galerie/', views.galerie, name='galerie'),
    path('universities/', views.universities, name='universities'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('bootstrap-gallery/', views.bootstrap_gallery, name='bootstrap-gallery'),
]