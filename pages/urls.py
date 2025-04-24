from django.urls import path
from .views import home, about, support


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('support/', support, name='support')
]
