from django.urls import path 
from .import views 


urlpatterns = [
    path('',views.studhome,name = 'studhome'),
    path('base/',views.base , name = 'base'),

]