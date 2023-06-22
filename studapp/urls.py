from django.urls import path 
from .import views 
from studapp.views import stud_list



urlpatterns = [
    path('',views.studhome,name = 'studhome'),
    path('base/',views.base , name = 'base'),
    path('Student/',stud_list.as_view(), name='stud_list'),

]

