from django.urls import path
from . import views



urlpatterns = [
    path('timeout/', views.timeout_view, name='timeout'),
    path('entrar/',views.login_view,name='login'),
    path('criar-conta/', views.register_view, name='register'),
    path('sair/', views.logout_view, name='logout'),

]



