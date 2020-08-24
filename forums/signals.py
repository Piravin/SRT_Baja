from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post
from django.core.mail import EmailMessage
from django.conf import settings 
from django.urls import reverse

def post_mail(sender,instance, created, **kwargs):
    if created:
        post_title, post_description = instance.title, instance.short_description
        subject = 'New post on : ' + post_title
        body_text = f"A new post on {post_title} was created \n A short description about the post: \n {post_description} \n Do check out the full post on srtbaja.in"
        body = f"<p>A new post on {post_title} was created</p><p> A short description about the post: </p><p> {post_description}</p><a href = 'http://srtbaja.in/forums/post/{instance.id}'>View post</a>"
        from_email = settings.EMAIL_HOST_USER
        to_mail = ['122004189@sastra.ac.in','jujukcmp@gmail.com']
        msg = EmailMessage(subject, body, from_email, to_mail)
        msg.content_subtype = 'html'
        msg.send(fail_silently=True)

post_save.connect(post_mail,sender=Post)