from django.contrib import admin
from django.urls import path
from .views import homepage, details

urlpatterns = [
    path('',homepage,name='home'),
    path('jobs/<int:job_id>',details,name='details')
]