from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=255)
    time_to_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description