from django.db import models
from django.contrib.auth.models import User

class StudySession(models.Model):
    subject = models.CharField(max_length=100)
    hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
    

