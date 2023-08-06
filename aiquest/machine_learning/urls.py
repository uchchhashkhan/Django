from django.urls import path
from . import views
urlpatterns = [
    path('machine/',views.machine_learning,name='machine'),
    path('rn/',views.random, name='rn'),
    path('knn/',views.k_nearest, name='knn'),
    path('dt/',views.dtree, name='dt'),
]