from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #MSK: Newly added
    path('about/', views.about, name='about'), #MSK: Newly added
    path('gems/', views.gems_index, name='index'), #MSK: Newly added
    path('gems/<int:gem_id>/', views.gems_detail, name='detail'), #MSK: route to showing details page
]