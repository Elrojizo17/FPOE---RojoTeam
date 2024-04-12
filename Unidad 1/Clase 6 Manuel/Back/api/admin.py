from django.contrib import admin
from .models.post import Post
from .models.mouse import Mouse
admin.site.register(Post)
admin.site.register(Mouse)