from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices


class Notes(models.Model):
    CATEGORY = Choices('Personal', 'Work', 'Education', 'Health')
    
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=150, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=0, blank=True)
    category = models.CharField(choices=CATEGORY, max_length=150, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

