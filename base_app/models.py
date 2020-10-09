from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=250)


class Question(models.Model):
    title = models.CharField(max_length=250)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    answer = models.CharField(max_length=100)
    note = models.TextField()

