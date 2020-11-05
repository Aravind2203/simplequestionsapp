from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    write=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=11999)
    problem=models.TextField()
    published_date=models.DateField(auto_now_add=True)
    class Meta:
        ordering=['-published_date']

    def __str__(self):
        return self.title

class Answers(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    answer=models.TextField()

    def __str__(self):
        return self.answer
