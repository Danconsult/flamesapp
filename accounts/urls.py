from .import views
from django.urls import path

urlpatterns = [
    path('signup/',views.signup, name = 'signup'),
    path('login/',views.logIn, name = 'login'),
    path('logout/',views.logOut, name = 'logout')
]