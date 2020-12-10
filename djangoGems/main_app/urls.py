from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #MSK: Newly added
    path('about/', views.about, name='about'), #MSK: Newly added
]