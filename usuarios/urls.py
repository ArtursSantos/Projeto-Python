from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastro, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('valida_login/', views.valida_login, name='valida_login'),
    path('sair/', views.sair, name='sair')
]