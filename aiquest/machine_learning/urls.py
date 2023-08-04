from django.urls import path
from . import views
urlpatterns = [
    path('machine/',views.machine_learning),
]