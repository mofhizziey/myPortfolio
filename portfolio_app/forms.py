from django import forms
from portfolio_app import models


    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    subject = forms.CharField(max_length=250)
    text = forms.CharField(max_length=2000, label='Description',
     help_text='Please fill in as much information as possible regarding any possible project collaborations or hire you have for me.',
     widget=forms.Textarea)
    sender = forms.EmailField(help_text='Please input your email address')



class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=250, help_text='Enter latest project name', label='Project Name')
    link = forms.CharField(max_length=250, help_text='My github link serves as a major portfolio showing alot of my past and current works.', label='Github link')
    class Meta:
        model = models.Project
        fields = ['name', 'screenshot', 'link', 'bio', 'url', 'web_host_type', 'web_host_provider']