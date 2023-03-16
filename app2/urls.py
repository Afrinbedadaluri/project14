from django.urls import path
from app2.views import *
app_name='one'
urlpatterns=[
    path('orenge/',orenge,name='orenge'),
]
