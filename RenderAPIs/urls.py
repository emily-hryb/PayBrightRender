from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authenticate', views.authenticate_page, name='authenticate'),    
    path('thanks', views.thanks, name='thanks')
]