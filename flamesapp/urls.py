from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name= 'app'),
    path('app/',views.app, name = 'app'),
    path('suggest/',views.suggest, name = 'suggest')
]