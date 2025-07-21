# posts/admin.py

from django.contrib import admin
from .models import Post

# Registra tu modelo aquí.
admin.site.register(Post)