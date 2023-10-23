from .views import *
from django.urls import path


urlpatterns = [
    path('',home, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('create/', Ceatepage.as_view(), name='create'),
    path('room/<int:pk>/', room, name='detail'),

]