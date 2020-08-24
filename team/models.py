from django.db import models
from ckeditor.fields import RichTextField

class Team(models.Model):
    year = models.CharField(max_length=20)
    photo = models.ImageField(default="default.jpg",upload_to="Teams")

    def __str__(self):
        return self.year


class Car(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    name = models.CharField(default='#',max_length=100)
    carpic = models.ImageField(default="default.png",upload_to="Cars",blank=True)
    def __str__(self):
        return self.team.year

class CarDetail(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    topic = models.CharField(max_length=100,blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return f"{self.car.team.year}-{self.topic}"
class Subsystem(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class TeamMember(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(default="default.png",upload_to="Team_profile_pics")
    role = models.CharField(max_length=100,default="member",blank=True)
    year_of_study = models.CharField(max_length=1)
    subsystem = models.ForeignKey(Subsystem, default=1,on_delete=models.SET_DEFAULT)
    linked_in = models.CharField(max_length=1000,default="#")
    description = models.TextField()

    def __str__(self):
        return self.name
