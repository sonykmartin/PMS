from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('test', views.test, name='test')
]