from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

STATUS = [
    ('in_progress', 'In progress'),
    ('completed','completed'),
    ('cancelled','cancelled')
]
# USER = 

class ModelTask(models.Model):
    user = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.task_name
