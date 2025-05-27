from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),                  # landing page with search form
    path('search/', views.search_results, name='search_results'),  # results page
    path('hostel/<int:hostel_id>/', views.hostel_detail, name='hostel_detail'),  # details page
]
