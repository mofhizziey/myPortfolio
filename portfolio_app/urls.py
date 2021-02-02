from django.urls import path
from portfolio_app import views
app_name = 'portfolio_app'


urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('my-projects/<slug:slug>', views.ProjectDetailView.as_view(), name='projects'),
    path('update/<slug:slug>', views.ProjectUpdateView.as_view(), name='update'),
    path('new-project/', views.ProjectCreateView.as_view(), name='create'),
]
