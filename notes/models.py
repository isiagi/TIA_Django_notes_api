from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices


class Notes(models.Model):
    CATEGORY = Choices('Personal', 'Work', 'Education', 'Health')
    PRIORITY = Choices('High', 'Moderate', 'Low')
    
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(choices=PRIORITY, max_length=150, null=True, blank=True, default=PRIORITY.Low)
    category = models.CharField(choices=CATEGORY, max_length=150, null=True, blank=True)
    user_email = models.EmailField(null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title
    

