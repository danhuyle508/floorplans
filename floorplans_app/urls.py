from django.urls import path
from .views import ProjectView


urlpatterns = [
    path('project', ProjectView, name='project_view'),
]