from django.urls import path
from .views import *

urlpatterns = [
    path('post-job/', post_job, name='post-job'),
    path('edit-job/<str:pk>/', edit_job, name='edit-job'),
    path('delete-job/<str:pk>/', delete_job, name='delete-job'),
    path('job-profile/<str:pk>/', job_profile, name='job-profile'),
    path('job-profile/applicant-list/<str:pk>/', applicant_list, name='applicant-list'),
]
