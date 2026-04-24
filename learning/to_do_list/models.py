from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=1000)
    #to check if the task is completed or not
    completed = models.BooleanField(default=False)
    #deadline
    deadline = models.DateTimeField(null=True, blank=True) #custom dates
    #created_at = models.DateTimeField(auto_now_add=True) #automatically add the date when the task is created
    def __str__(self):
        return self.title 
