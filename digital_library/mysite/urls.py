from django.urls import path

from . import views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('registration/login', views.login, name='login'),
]
