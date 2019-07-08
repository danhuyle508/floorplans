from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy    

# Create your views here.

class ProjectView(LoginRequiredMixin):
    template_name = 'projects/projects_list.html'
    context_object_anme = 'projects'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Project.objects.filter(user__username=self.request.user.username)
