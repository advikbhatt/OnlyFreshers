from django.urls import path
from .views import quiz_view, success_view

urlpatterns = [
    path('', quiz_view, name='quiz'),
    path('success/', success_view, name='success'),
    
]
