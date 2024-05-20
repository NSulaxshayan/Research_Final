from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_network, name='scan_network'),
    path('pulse_view/', views.pulse_view, name='pulse_view'),
]
