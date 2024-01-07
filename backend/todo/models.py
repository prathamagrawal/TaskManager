from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=120)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

# Create your models here.
