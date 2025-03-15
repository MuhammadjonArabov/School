from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='main'),
    path('active-student/', views.active_student_list, name='active_student_list'),
    path('teachers-list/', views.teachers_list, name='teachers_list'),
    path('faces-of-school/', views.faces_of_school, name='faces_of_school'),
    path('', views.background_view, name='background'),

]