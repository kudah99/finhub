from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='learn'),
    path('login',  views.UserLoginView.as_view(), name='login'),
    path('logout', views.signout, name='logout'),
    path('register', views.UserRegistration.as_view(), name='register'),
    path('enroll_start', views.enroll_start, name='enroll_start'),
    path('learn_start', views.learn_start, name='learn_start'),
    path('learning_resources', views.learning_resources, name="learning_resources"),
    path('my-coarses', views.my_coarses, name="my_coarses"),
    path('resources', views.finServicesCategory, name="resources"),
    path('learning_resources_details', views.learning_resources_details, name="learning_resources_details"),
]