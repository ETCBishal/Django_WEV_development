from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('login/', views.signupUser,name='login'),
    path('signin/', views.loginUser,name='signin'),
    path('flavours/', views.flavour,name='flavour'),
]