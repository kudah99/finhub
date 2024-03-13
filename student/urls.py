from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='learn'),
    path('login', views.signin, name='login'),
    path('logout', views.signout, name='logout'),
    path('register', views.register, name='register'),
    path('enroll_start', views.enroll_start, name='enroll_start'),
    path('learn_start', views.learn_start, name='learn_start')
]