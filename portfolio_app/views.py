from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from portfolio_app import models

def contact(request):
    if request.POST == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['Sender']
            subject = form.cleaned_data['Subject']
            text = form.cleaned_data['Text']
            recipients = "mofeodujirin@gmail.com"
            send_mail(subject, text, sender, recipients)
            
            return reverse('portfolio_app:contact')
    else:
        form = ContactForm()

    return render(request, "portfolio_app/contact.html", {"form":form})

def projects(request):
    return render(request, "portfolio_app/projects.html")

class ProjectListView(ListView):
    ordering = '-date_created'
    model = models.Project
    template_name = 'portfolio_app/index.html'

class ProjectDetailView(DetailView):
    model = models.Project
    template_name = 'portfolio_app/projects.html'


class ProjectCreateView(CreateView):
    model = models.Project
    template_name = 'portfolio_app/new_project.html'
    fields = ['name', 'screenshot', 'bio', 'url', 'link']


class ProjectUpdateView(UpdateView):
    model = models.Project
    template_name = 'portfolio_app/update_projects.html'
    fields = ['name', 'screenshot', 'bio', 'url', 'link']
