from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from Hangarin_app.models import Task,SubTask,Priority, Category, Note
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Hangarin_app.forms import TaskForm, SubTaskForm, PriorityForm, CategoryForm, NoteForm



class HomePageView(LoginRequiredMixin,ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.count()
        context["completed_tasks"] = Task.objects.filter(status="Completed").count()
        context["pending_tasks"] = Task.objects.filter(status="Pending").count()
        context["total_subtasks"] = SubTask.objects.count()
        return context

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(task_title__icontains=query) |      
                Q(descript__icontains=query) |        
                Q(deadline__icontains=query) |
                Q(status__icontains=query) |
                Q(category__category_name__icontains=query) | 
                Q(priority__priority_name__icontains=query) 
             )
        return qs
    
    def get_ordering(self):
        allowed = ["task_title", "status","deadline", "category__name", "priority__name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "task_title"

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')
    
class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = 'sub_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(status__icontains=query)
                )
        return qs
    
    def get_ordering(self):
        allowed = ["title","status"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "parent_task__task_title"

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'sub_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'sub_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'sub_del.html'
    success_url = reverse_lazy('subtask-list')

class PriorityList(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'prio_list.html'
    paginate_by = 10


class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'prio_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'prio_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'prio_del.html'
    success_url = reverse_lazy('priority-list')

class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'cat_list.html'
    paginate_by = 10

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cat_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cat_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'cat_del.html'
    success_url = reverse_lazy('category-list')

class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by')

        # filtering
        if query:
            qs = qs.filter(
                Q(task__task_title__icontains=query) |
                Q(contents__icontains=query)
            )

        # sorting
        allowed = ["task__task_title", "contents"]
        if sort_by in allowed:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("task__task_title")

        return qs

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_form.html'
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes_del.html'
    success_url = reverse_lazy('note-list')