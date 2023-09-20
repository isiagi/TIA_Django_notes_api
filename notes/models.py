from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

