from django.contrib import admin
from .models import Todo
from .models import Task

admin.site.register(Todo)
admin.site.register(Task)