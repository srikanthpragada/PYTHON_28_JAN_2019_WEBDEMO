from django.urls import path
from . import views, hr_views, titles_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('course/', views.show_course),
    path('countries/', views.list_countries),
    path('jobs/', hr_views.list_jobs),
    path('addjob/', hr_views.add_job),
    path('addjob2/', hr_views.add_job_with_form),
    path('titles/home/', titles_views.titles_home),
    path('titles/list/', titles_views.titles_list),
    path('titles/add/', titles_views.titles_add),
    path('titles/delete/<int:id>', titles_views.titles_delete),
]

