from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    result = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="test", default=None)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.question    