from . import views
from django.urls import path


app_name = 'home_module'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('user-register/', views.UserRegisterView.as_view(), name='registration'),
    path('user-login/', views.UserLoginView.as_view(), name='log_in'),
    path('user-logout/', views.UserLogOutView.as_view(), name='log_out'),
]
