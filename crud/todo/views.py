from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import TodoApp

# Create your views here.
# class based view
class TodoAppCreateView(CreateView):
    # specify the model for create view
    model = TodoApp

    # specify the fields
    fields = [
        'title',
        'description'
    ]

    template_name = 'home.html'
    success_url = "list"


# list view
class TodoAppListView(ListView):
    model = TodoApp
    template_name = 'list.html'


# detail view
class TodoAppDetailView(DetailView):
    model = TodoApp
    template_name = 'detail.html'


# update view
class TodoAppUpdateView(UpdateView):
    model = TodoApp
    # fields that can be edited
    fields = [
        "title",
        "description"
    ]
    template_name = 'update.html'
    success_url = "/"

# delete view
class TodoAppDeleteView(DeleteView):
    model = TodoApp
    template_name = 'delete.html'
    success_url = "/"