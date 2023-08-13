from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

# Create todo models 

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='todos')
    title = models.TextField()
    complated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering  = ['-id']
        
        
    
    
