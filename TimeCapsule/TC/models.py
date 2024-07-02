from django.db import models
from django.contrib.auth .models import User
# Create your models here.
class TimeCapsule(models.Model):
    status_choice = [
        ('private' ,'private'),
        ('public' ,'public')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="User")
    title = models.TextField(max_length=50, default="")
    status = models.CharField(choices=status_choice,max_length=20)
    collaborators = models.ForeignKey(User,on_delete=models.CASCADE,related_name='shared_users',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    future_date = models.DateTimeField()
    text = models.TextField(max_length=500,blank=True)
    force_open_pass = models.TextField(max_length=100)
    image1 = models.ImageField(upload_to='images',blank=True,null=True)
    image2 = models.ImageField(upload_to='images',blank=True,null=True)
    video1 = models.FileField(upload_to='videos', blank=True,null=True)
    video2 = models.FileField(upload_to='videos', blank=True,null=True)
    is_sealed = models.BooleanField()
    is_force_opened = models.BooleanField()

    def __str__(self):
        return self.user.username + " " + self.title

