from django.urls import path
from . import views

urlpatterns = [
    path('', views.cert_info),
    path('output', views.output, name='script1'),
    path('ctacert', views.cert_info, name='ctacert'),
]
