from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    def __str__(self):
        return self.title + ' - ' + self.user.username

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) #if no text is passed -> ''
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True) #blank=True for the admin, null=True for de db
    isImportant = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)