from django.contrib import admin
from .models.post import Post
from .models.moto import Moto

admin.site.register(Post)
admin.site.register(Moto)