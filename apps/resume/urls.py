from django.urls import path
from .views import resume_view

app_name = 'resume'

urlpatterns = [
    path('', resume_view, name='resume'),
]