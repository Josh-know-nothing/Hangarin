"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Hangarin_app.views import (
                            TaskList, TaskCreateView, TaskUpdateView, TaskDeleteView,
                            SubTaskList, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView,
                            PriorityList, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
                            CategoryList, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
                            NoteList, NoteCreateView, NoteUpdateView, NoteDeleteView
                            )
from Hangarin_app import views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('accounts/',include('allauth.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', views.HomePageView.as_view(), name='home'),
    path('task_list', TaskList.as_view(), name='task-list'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('sub_list', SubTaskList.as_view(), name='subtask-list'),
    path('sub_list/add', SubTaskCreateView.as_view(), name='subtask-add'),
    path('sub_list/<pk>', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('sub_list/<pk>/delete', SubTaskDeleteView.as_view(), name='subtask-delete'),
    path('prio_list', PriorityList.as_view(), name='priority-list'),
    path('prio_list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('prio_list/<pk>', PriorityUpdateView.as_view(), name='priority-update'),
    path('prio_list/<pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'),
    path('cat_list', CategoryList.as_view(), name='category-list'),
    path('cat_list/add', CategoryCreateView.as_view(), name='category-add'),
    path('cat_list/<pk>', CategoryUpdateView.as_view(), name='category-update'),
    path('cat_list/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
    path('notes_list', NoteList.as_view(), name='note-list'),
    path('notes_list/add', NoteCreateView.as_view(), name='note-add'),
    path('notes_list/<pk>', NoteUpdateView.as_view(), name='note-update'),
    path('notes_list/<pk>/delete', NoteDeleteView.as_view(), name='note-delete'),
]