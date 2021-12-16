from django.db import models
from django.urls import reverse
import datetime

class Registration(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    user_name = models.CharField(unique=True,max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.user_name

class Blog(models.Model):
    username = models.ForeignKey(Registration, on_delete=models.CASCADE)
    post = models.TextField()
    title = models.CharField(max_length=50)
    date = models.DateField(("Date"), default=datetime.date.today)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('update',kwargs={'pk':self.pk})