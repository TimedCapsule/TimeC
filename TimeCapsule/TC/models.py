from django.db import models
from django.contrib.auth .models import User
# Create your models here.
class TimeCapsule(models.Model):
    status_choice = [
        ('private' ,'private'),
        ('public' ,'public')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="User")
    status = models.CharField(choices=status_choice,max_length=20)
    collaborators = models.ForeignKey(User,on_delete=models.CASCADE,related_name='shared_users',blank=True)
    created_at = models.TimeField(auto_now_add=True)
    future_date = models.DateTimeField()
    text = models.TextField(max_length=500,blank=True)
    image1 = models.ImageField(upload_to='media/images',blank=True)
    image2 = models.ImageField(upload_to='media/images',blank=True)
    video1 = models.CharField(max_length=300,blank=True)
    video2 = models.CharField(max_length=300,blank=True)
    is_sealed = models.BooleanField()

    def __str__(self):
        return self.user.username

