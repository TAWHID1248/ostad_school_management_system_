from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.StudentListViews.as_view(), name='home'),
    path('form/', views.AddStudentView.as_view(), name='student-form'),
    # path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:id>/update', views.StudentUpdateViews.as_view(), name='student-update'),
    path('student/<int:id>/delete', views.StudentDeleteViews.as_view(), name='student-delete'),
    

]