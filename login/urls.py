from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addempresa/', views.addempresa, name='addempresa'),
    path('enviarfinancas/', views.enviarfinancas, name='enviarfinancas'),
]
