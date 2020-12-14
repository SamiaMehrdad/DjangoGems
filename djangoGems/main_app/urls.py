from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #MSK: Newly added
    path('about/', views.about, name='about'), #MSK: Newly added
    path('gems/', views.gems_index, name='index'), #MSK: Newly added
    path('gems/<int:gem_id>/', views.gems_detail, name='detail'), #MSK: route to showing details page
    #MSK: new route used to show a create-form using CBT
    path('gems/create/', views.GemCreate.as_view(), name='gems_create'),
    path('gems/<int:pk>/update/', views.GemUpdate.as_view(), name='gems_update'),
    path('gems/<int:pk>/delete/', views.GemDelete.as_view(), name='gems_delete'),
    path('gems/<int:gem_id>/add_famous/', views.add_famous, name='add_famous'),
]