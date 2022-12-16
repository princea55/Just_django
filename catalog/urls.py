from django.contrib import admin
from django.urls import path, include

from .views import student_list, StudentListView, StudentDetailView

urlpatterns = [
    path('list_student/<int:page>/', StudentListView.as_view(), name='student-list'),
    path('student-detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail')
]
