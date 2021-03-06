from django.urls import path

from . import views, hr_views, titles_views, rest_views, class_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('course/', views.show_course),
    path('countries/', views.list_countries),
    path('jobs/', hr_views.list_jobs),
    path('addjob/', hr_views.add_job),
    path('addjob2/', hr_views.add_job_with_form),
    path('ajaxdemo/', views.ajax_demo),
    path('ajaxdatetime/', views.ajax_datetime),
    path('titles/home/', titles_views.titles_home),
    path('titles/list/', titles_views.titles_list),
    path('titles/add/', titles_views.titles_add),
    path('titles/delete/<int:id>', titles_views.titles_delete),
    path('titles/edit/<int:id>', titles_views.titles_edit),
    path('titles/searchform', titles_views.titles_search_form),
    path('titles/search', titles_views.titles_search),
    path('sessions/', views.session_names),
    path('api/titles/', rest_views.title_process),
    path('api/titles/<int:id>', rest_views.one_title_process),
    path('api/client', rest_views.rest_client),
    # Class based views
    path('hello/', class_views.HelloView.as_view()),
    path('titles/', class_views.ListTitles.as_view()),
]
