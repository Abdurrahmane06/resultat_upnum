# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil (Recherche)
    path('', views.consulter_resultats, name='consulter_resultats'), 
    
    # URL directe pour un relevé spécifique
    path('releve/<str:semestre>/<str:matricule>/', views.releve_generique, name='releve_generique'),
]
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('releve/s1/', views.releve_s1, name='releve_s1'),
#     path('releve/s2/', views.releve_s2, name='releve_s2'),
#     path('releve/s3/', views.releve_s3, name='releve_s3'),
#     path('releve/s4/', views.releve_s4, name='releve_s4'),
# ]