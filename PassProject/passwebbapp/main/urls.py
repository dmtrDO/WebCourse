
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('history', views.history, name='history'),
    path('delete/<int:pk>/', views.delete_password, name='delete'),
    path('update/', views.update_association, name='update')
]



