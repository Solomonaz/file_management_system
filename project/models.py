from django.db import models
from account.models import Account


STATUS = (
    ('pending','Pending'),
    ('on-hold','On-hold'),
    ('done','Done'),
)


class Project_List(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    users = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    



