from django.urls import path, include
from app1.views import *

urlpatterns = [
  path('Data/',NewData,name='cals'),  
  path('',Index,name='home'),
  path('About_us/',About_us,name='about'),
  path('Blogs/',Blog,name='blog'),
  path('Contact_us/',Contact_us,name='contact'),
]
