from django.db import models
from PIL import Image

class Item(models.Model):
    logo = models.ImageField(default='logo.png',upload_to='logo',blank=True)
    quote1 = models.CharField(default="SASTRA Racing Team - Baja", max_length=50) 
    quote2 = models.CharField(default="Quotes comming soon..", max_length=100,blank=True)
    backgroundimage1 = models.ImageField(default='back1.jpg',upload_to='back1',blank=True)
    video = models.CharField(max_length=1000,blank=True)
    video_description = models.TextField(blank=True)
    contacts = models.TextField(blank=True)
    team_background = models.ImageField(default='back2.jpg',upload_to='team',blank=True)


class Slide(models.Model):
    title = models.CharField(max_length=100)
    slide_link = models.CharField(max_length=1000,default='#', blank=True)
    slide = models.ImageField(upload_to='slides')

    def __str__(self):
        return self.title

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    sponsor = models.ImageField(upload_to="sponsors")
    link = models.CharField(max_length=1000,default="#")

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField(blank=True)
    subject = models.TextField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    phone_no = models.CharField(max_length=12)
    twitter = models.CharField(max_length=1000)
    facebook = models.CharField(max_length=1000)
    instagram = models.CharField(max_length=1000)
    email = models.EmailField()


