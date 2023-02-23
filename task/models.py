from django.db import models
from project.models import Project_List
from account.models import Account

STATUS = (
    ('pending','Pending'),
    ('on-hold','On-hold'),
    ('done','Done'),
)


class Task_List(models.Model):
    project = models.ForeignKey(Project_List, on_delete=models.CASCADE, related_name='project_lists')
    assigne = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class Productivity(models.Model):
#     project  = models.ForeignKey(Project_List, related_name='project_list',on_delete=models.CASCADE)
#     task = models.ForeignKey(Task_List, related_name='task_list',on_delete=models.CASCADE)
#     # assigne = models.ForeignKey(Account, related_name='tasks')
#     comment = models.TextField()
#     date  = models.DateTimeField()
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.project
    
