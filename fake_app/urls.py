
from django.urls import path
from .views import *

urlpatterns = [

    path('fake/',Fake_view,name='fake'),
    path('data/',display_data,name='data'),
]
