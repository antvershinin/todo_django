from django.shortcuts import render
from .models import Todo
# Create your views here.


def index(request):
    todos_list = Todo.objects.all()
    context = {
        "todo_list": todos_list
    }
    return render(request, template_name='todo/index.html', context=context)


def filter(request, filterName):
    if filterName == "active":
        todos_list = Todo.objects.filter(is_completed=False)
    elif filterName == "completed":
        todos_list = Todo.objects.filter(is_completed=True)
    context = {
        "todo_list": todos_list
    }
    return render(request, template_name='todo/filter.html', context=context)
