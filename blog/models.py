from pyexpat import model
from venv import create
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=255
    )
    
    slug = models.SlugField(
        max_length=255, 
        unique=True
    ) # www.meusite.com/blog/intrducao-ao-django
    
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    
    body = models.TextField()
    
    create = models.DateTimeField(
        auto_now_add=True
    )
    
    updated = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return self.title
    