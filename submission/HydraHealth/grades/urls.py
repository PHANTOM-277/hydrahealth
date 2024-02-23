from django.urls import path
from . import views

app_name='grades'
urlpatterns = [
    #dashboard
    path('dashboard/',views.dashboard,name='dashboard'),
    path('topic1/',views.topic1,name='topic1'),
    path('topic2/',views.topic2,name='topic2'),
    path('topic3/',views.topic3,name='topic3'),
]