from django.urls import path
from . import views
urlpatterns = [
    path('del/',views.deep_learning, name='deep'),
    path('reg/', views.registration)
]