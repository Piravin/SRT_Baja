from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 1000)
    short_description = models.TextField()
    content = RichTextField()
    writer = models.ForeignKey(User,null = True,on_delete=models.SET_NULL)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name = 'comments',on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User,null= True,on_delete=models.SET_NULL)
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username + '--' + self.post.title + str(self.id))

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.post.id})