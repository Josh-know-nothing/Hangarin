from django.contrib import admin


# Register your models here.
from .models import Category,Priority,Task,Note,SubTask

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ("title", "status")
    show_change_link = True

class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    fields = ("contents", "created_at")
    readonly_fields = ("created_at",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)

@admin.register(Priority)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("priority_name",)
    search_fields = ("priority_name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_title", "status", "deadline", "priority", "category")
    list_filter = ("status", "priority", "category")
    search_fields = ("task_title", "descript")

    inlines = [SubTaskInline, NoteInline]
    
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("task", "contents", "created_at")
    list_filter = ("created_at",)
    search_fields = ("contents",)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "parent_task")
    list_filter = ("status",)
    search_fields = ("title",)