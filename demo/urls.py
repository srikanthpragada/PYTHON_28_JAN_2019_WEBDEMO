from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('course/', views.show_course),
    path('countries/', views.list_countries),
]
