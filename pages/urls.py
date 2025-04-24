from django.urls import path
from .views import home, about, support, services


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('support/', support, name='support'),
    path('servises/', services, name='servises')
]
