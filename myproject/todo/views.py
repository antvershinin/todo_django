from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
# Create your views here.


def index(request):
    todos_list = Todo.objects.filter(is_active=False)
    output = ', '. join(el.text for el in todos_list)
    return render(request, template_name='todo/index.html')
