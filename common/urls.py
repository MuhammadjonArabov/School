from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='main'),
    path('active-student/', views.active_student_list, name='active_student_list'),
    path('', views.background_view, name='background'),

]