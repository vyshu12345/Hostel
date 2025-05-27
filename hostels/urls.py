from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),                 
    path('search/', views.search_results, name='search_results'),  
    path('hostel/<int:hostel_id>/', views.hostel_detail, name='hostel_detail'), 
]
