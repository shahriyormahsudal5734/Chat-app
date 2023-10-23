from django.db import models
from django.contrib.auth.models import User
from requests import request
class Room(models.Model):
    host = models.ForeignKey(User ,default=User, on_delete=models.SET_NULL, auto_created=True, null=True)
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='room/')
    descreption = models.TextField(null=True,blank=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    class Meta :
        ordering = ['-createdtime']

    def __str__(self):
        return str(self.name) 


class Message(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='imgmessage/',default='0')
    class Meta :
        ordering = ['-createdtime']

    def __str__(self):
        return str(self.body) 
    
