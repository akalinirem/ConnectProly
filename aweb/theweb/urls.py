from django.urls import path
from django.shortcuts import render
from . import views

def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('home/', home),
    path('', views.index, name='index'),
    # Diğer yol desenleriniz

]