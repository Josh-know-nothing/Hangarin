from django.contrib import admin
from .models import Category,Priority,Task,Note,SubTask

# Register your models here.
admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Task)
admin.site.register(Note)
admin.site.register(SubTask)