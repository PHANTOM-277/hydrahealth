from django.urls import path, include
from . import views

app_name='home'
urlpatterns = [
    path('',views.homee,name='homee'),
    path('about_us',views.about_us,name='about_us'),
]