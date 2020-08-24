from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    class Meta:
        js = ('tinymceinject.js')

