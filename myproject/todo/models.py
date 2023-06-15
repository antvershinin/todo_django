from django.db import models
from datetime import datetime

# Create your models here.


class Todo(models.Model):
    text = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
