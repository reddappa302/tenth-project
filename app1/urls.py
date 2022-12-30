from django.urls import path
from app1.views import *
app_name='red'

urlpatterns=[
    path('crr/',crr,name='crr'),
    path('yh/',yh,name='yh'),
]