from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
# Create your models here.
from django.utils import timezone

WEB_HOST_TYPE = [
    ('Cloud', 'Cloud'),
    ('VPS', 'VPS'),
    ('Shared Hosting', 'Shared Hosting'),
]

class Project(models.Model):
    name = models.CharField(max_length=250)
    screenshot = models.ImageField(upload_to='Project Images')
    bio = models.TextField()
    url =  models.CharField(max_length=250)
    link = models.CharField(max_length=250, null=True)
    slug = models.SlugField()
    date_created = models.DateTimeField(default=timezone.now())
    web_host_type = models.CharField(max_length=250, choices=WEB_HOST_TYPE, default='Cloud')
    web_host_provider = models.CharField(max_length=250, null=True)

    def get_absolute_url(self):
        return reverse('portfolio_app:projects', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}')
        return super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    text = models.TextField()
    sender = models.EmailField()
    message_date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')

